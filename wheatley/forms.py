# -*- coding: UTF-8 -*-

import os

from django import forms
from wheatley.models import Location, Photo, Tweet, Settings

class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = ['title', 'latitude', 'longitude', 'elevation']

class PhotoForm(forms.ModelForm):
	SIZE = (
			(u'640x480', u'640x480'),
			(u'567x480', u'567x480'),
			(u'720x576', u'720x567'),
			(u'1920x1080', u'1920x1080'),
			(u'1920x1200', u'1920x1200'),
	)
	size = forms.CharField(max_length=255, widget=forms.Select(choices=SIZE))

	# ugly fuck :P
	def get_raspistill(self):
		settings = Settings.objects.latest('created_at')
		raspistill = settings.get_raspistill()

		cmd = "%s --width %s --height %s --quality %s" % (raspistill,
				self.data['width'], self.data['height'],
				self.data['quality'])
		cmd = "%s --imxfx %s --metering %s --exposure %s --awb %s" % (cmd,
				self.data['imxfx'], self.data['metering'],
				self.data['exposure'], self.data['awb'])
		cmd = "%s --sharpness %s --contrast %s --brightness %s" % (cmd,
				self.data['sharpness'], self.data['contrast'],
				self.data['brightness'])
		cmd = "%s --saturation %s --rotation %s" % (cmd,
				self.data['saturation'], self.data['rotation'])

		if 'hflip' in self.data.keys():
			cmd = "%s --hflip" % (cmd)
		if 'vflip' in self.data.keys():
			cmd = "%s --vflip" % (cmd)

		cmd = "%s --output %s" % (cmd, os.path.join(settings.media_path, self.data['filename']))

		return cmd

	class Meta:
		model = Photo
		fields = ['filename', 'width', 'height', 'quality', 'imxfx',
		'metering', 'exposure', 'awb', 'sharpness', 'contrast', 'brightness',
		'saturation', 'rotation', 'hflip', 'vflip', 'size',]

class TweetForm(forms.ModelForm):
	class Meta:
		model = Tweet
		fields = ['status', 'hashtag']
		widgets = {
				'status': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
		}

# vim: set ft=python ts=4 sw=4 :
