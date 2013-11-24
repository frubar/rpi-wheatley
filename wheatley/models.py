# -*- coding: UTF-8 -*-

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Settings(models.Model):
	class Meta:
		ordering = ['created_at']
		verbose_name_plural = 'settings'

	def __unicode__(self):
		return ('')

	ENCODING = (
			(u'jpg', u'jpg'),
			(u'png', u'png'),
			(u'gif', u'gif'),
			(u'bmp', u'bmp'),
	)

	created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)
	control_addr = models.GenericIPAddressField()
	media_path = models.CharField(max_length=255)
	camera_binary = models.CharField(max_length=255)
	camera_timeout = models.SmallIntegerField()
	camera_encoding = models.CharField(max_length=255, choices=ENCODING,
			default='jpg')
	camera_extras = models.CharField(max_length=255, blank=True, null=True)
	twitter_consumer_key = models.CharField(max_length=255)
	twitter_consumer_secret = models.CharField(max_length=255)
	twitter_access_token = models.CharField(max_length=255)
	twitter_access_token_secret = models.CharField(max_length=255)

	def get_raspistill(self):
		raspistill = "%s -t %s -e %s" % (self.camera_binary,
				self.camera_timeout, self.camera_encoding)
		if self.camera_extras:
			raspistill = "%s %s" % (raspistill, self.camera_extras)

		return raspistill


class Location(models.Model):
	class Meta:
		ordering = ['-created_at', 'title']

	def __unicode__(self):
		return ('%s') % (self.title)

	created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)
	title = models.CharField(max_length=255)
	latitude = models.FloatField()
	longitude = models.FloatField()
	elevation = models.DecimalField(max_digits=6, decimal_places=1, blank=True,
			null=True)

class Photo(models.Model):
	class Meta:
		ordering = ['-created_at', 'filename']

	def __unicode__(self):
		return '%s' % (self.filename)

	IMXFX = (
		(u'none', u'none'),
		(u'negative', u'negative'),
		(u'solarise', u'solarise'),
		(u'sketch', u'sketch'),
		(u'denoise', u'denoise'),
		(u'emboss', u'emboss'),
		(u'oilpaint', u'oilpaint'),
		(u'hatch', u'hatch'),
		(u'gpen', u'gpen'),
		(u'pastel', u'pastel'),
		(u'watercolour', u'watercolour'),
		(u'film', u'film'),
		(u'blur', u'blur'),
		(u'saturation', u'saturation'),
		(u'colourswap', u'colourswap'),
		(u'washedout', u'washedout'),
		(u'posterise', u'posterise'),
		(u'colourpoint', u'colourpoint'),
		(u'colourbalance', u'colourbalance'),
		(u'cartoon', u'cartoon'),
	)

	METERING = (
		(u'average', u'average'),
		(u'spot', u'spot'),
		(u'backlit', u'backlit'),
		(u'matrix', u'matrix'),
	)

	EXPOSURE = (
		(u'auto', u'auto'),
		(u'night', u'night'),
		(u'nightpreview', u'nightpreview'),
		(u'backlight', u'backlight'),
		(u'spotlight', u'spotlight'),
		(u'sports', u'sports'),
		(u'snow', u'snow'),
		(u'beach', u'beach'),
		(u'verylong', u'verylong'),
		(u'fixedfps', u'fixedfps'),
		(u'antishake', u'antishake'),
		(u'fireworks', u'fireworks'),
	)

	AWB = (
		(u'auto', u'auto'),
		(u'off', u'off'),
		(u'sun', u'sun'),
		(u'cloud', u'cloud'),
		(u'shade', u'shade'),
		(u'tungsten', u'tungsten'),
		(u'fluorescent', u'fluorescent'),
		(u'incandescent', u'incandescent'),
		(u'flash', u'flash'),
		(u'horizon', u'horizon'),
	)

	created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)
	filename = models.CharField(max_length=255)
	width = models.SmallIntegerField()
	height = models.SmallIntegerField()
	quality = models.SmallIntegerField(default=85)
	imxfx = models.CharField(max_length=255, choices=IMXFX,
		default='none')
	metering = models.CharField(max_length=255, choices=METERING,
		default='average')
	exposure = models.CharField(max_length=255, choices=EXPOSURE,
		default='auto')
	awb = models.CharField(max_length=255, choices=AWB, default='auto')
	sharpness = models.SmallIntegerField(default=0)
	contrast = models.SmallIntegerField(default=0)
	brightness = models.SmallIntegerField(default=50)
	saturation = models.SmallIntegerField(default=0)
	rotation = models.SmallIntegerField(default=0)
	hflip = models.BooleanField(default=False)
	vflip = models.BooleanField(default=False)
	location = models.ForeignKey(Location, blank=True, null=True)

class Tweet(models.Model):
	class Meta:
		ordering = ['-created_at']

	def __unicode__(self):
		return '%s%s' % (self.status[:17], '...')

	created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)
	status = models.CharField(max_length=100, blank=True)
	hashtag = models.CharField(max_length=15, blank=True)
	photo = models.ForeignKey(Photo, blank=True, null=True)
	location = models.ForeignKey(Location, blank=True, null=True)

# vim: set ft=python ts=4 sw=4 :
