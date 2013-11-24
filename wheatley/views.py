# -*- coding: UTF-8 -*-

from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.http import HttpResponseBadRequest, HttpResponseRedirect

from wheatley.models import Location, Photo, Tweet, Settings
from wheatley.forms import LocationForm, PhotoForm, TweetForm

import os
import datetime
import uuid
import subprocess
from twython import Twython

class SettingsView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse('<h1>Settings</h1>')

	def post(self, request, *args, **kwargs):
		return HttpResponse('<h1>Settings</h1>')

class IndexView(View):
	template = 'index.html'
	context = {}
	settings = None

	def _read_settings(self):
		try:
			self.settings = Settings.objects.latest('created_at')
		except:
			return False
		return True

	def _has_permission(self, request):
		if self.settings.control_addr == request.META['REMOTE_ADDR']:
			self.context.update(control=True)

	def _take_photo(self, cmd):
		call = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE,
				stderr=subprocess.PIPE)
		raw, err = call.communicate()
		if err:
			return False
		return True

	def _shot(self, request):
		attributes = request.POST.copy()

		# create unique filename
		filename = "%s-%s.%s" % (str(uuid.uuid4()),
				datetime.datetime.now().strftime("%s"),
				self.settings.camera_encoding)
		attributes.update(filename=filename)

		# get width, height
		width, height = attributes.__getitem__('size').split('x')
		attributes.update(width=width)
		attributes.update(height=height)

		form = PhotoForm(attributes)
		if form.is_valid:
			cmd = form.get_raspistill()
			if self._take_photo(cmd):
				form.save()
				photo = os.path.join('/static/media', filename)
				self.context.update(photo=photo)
				forms = {
						'photo': PhotoForm(request.POST),
						'tweet': TweetForm()
				}
				self.context.update(forms=forms)

	def _tweet(self, request):
		attributes = request.POST.copy()

		# verify status and take action if necessary
		status = attributes.__getitem__('status')
		hashtag = attributes.__getitem__('hashtag')
		if len(status) > 100:
			status = "%s %s" % (status[:96], "...")
		attributes.update(status=status)

		# get last shot
		try:
			photo = Photo.objects.latest('created_at')
		except:
			photo = None

		# get location
		try:
			location = Location.objects.latest('created_at')
		except:
			location = None

		twitter = Twython(self.settings.twitter_consumer_key,
				self.settings.twitter_consumer_secret,
				self.settings.twitter_access_token,
				self.settings.twitter_access_token_secret)
		if photo:
			photofile = os.path.join(self.settings.media_path, str(photo))
			with open(photofile, 'rb') as media:
				status = "%s %s" % (status, hashtag)
				tweet = twitter.update_status_with_media(status=status,
						media=media, lat=location.latitude, lon=location.longitude)
				attributes.update(photo=photo)
		else:
			status = "%s %s" % (status, hashtag)
			tweet = twitter.update_status(status=status,
					lat=location.latitude, lon=location.longitude)

		url = 'https://twitter.com/rpiwheatley/status/' + str(tweet['id'])
		self.context.update(url=url)

		form  = TweetForm(attributes)
		form.save()

		forms = {
				'photo': PhotoForm(),
				'tweet': TweetForm()
		}
		self.context.update(forms=forms)

	def get(self, request, *args, **kwargs):
		if not self._read_settings():
			return redirect('settings')
		self.context = {}
		self._has_permission(request)
		forms = {
				'photo': PhotoForm(),
				'tweet': TweetForm(),
		}
		self.context.update(forms=forms)
		return render(request, self.template, self.context)

	def post(self, request, *args, **kwargs):
		if not self._read_settings():
			return redirect('settings')
		self.context = {}
		if request.POST.__contains__('shot'):
			self._shot(request)
		elif request.POST.__contains__('tweet'):
			self._tweet(request)
		self._has_permission(request)
		return render(request, self.template, self.context)

# vim: set ft=python ts=4 sw=4 :
