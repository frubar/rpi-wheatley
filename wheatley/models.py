# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone

class Photo(models.Model):
	class Meta:
		ordering = ['-created_date', 'filename']

	def __unicode__(self):
		return '%s' % (self.filename)

	ENCODING_CHOICES = (
		(u'jpg', u'jpg'),
		(u'bmp', u'bmp'),
		(u'gif', u'gif'),
		(u'png', u'png'),
	)

	EFFECT_CHOICES = (
		(u'none', u'none'),
		(u'negative', u'negative'),
		(u'solarise', u'solarise'),
		(u'skecth', u'sketch'),
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

	created_date = models.DateTimeField(default=timezone.now, auto_now_add=True)
	filename = models.CharField(max_length=255)
	width = models.PositiveSmallIntegerField()
	height = models.PositiveSmallIntegerField()
	encoding = models.CharField(max_length=255, choices=ENCODING_CHOICES,
		default='jpg')
	effect = models.CharField(max_length=255, choices=EFFECT_CHOICES,
		default='none')
	size = models.DecimalField(max_digits=19, decimal_places=2)

class Location(models.Model):
	class Meta:
		ordering = ['-created_date', 'description']

	def __unicode__(self):
		return '%s' % (self.description)

	created_date = models.DateTimeField(default=timezone.now, auto_now_add=True)
	description = models.CharField(max_length=255)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	altitude = models.FloatField(blank=True, null=True)

class Shot(models.Model):
	class Meta:
		ordering = ['-created_date', 'location']

	def __unicode__(self):
		return '%d' % (self.id)

	created_date = models.DateTimeField(default=timezone.now, auto_now_add=True)
	photo = models.OneToOneField(Photo)
	location = models.ForeignKey(Location)

class Voice(models.Model):
	class Meta:
		ordering = ['-id']

	def __unicode__(self):
		return '%d' % (self.id)

	text = models.TextField()

class Tweet(models.Model):
	class Meta:
		ordering = ['-created_date']

	def __unicode__(self):
		return '%d' % (self.id)

	created_date = models.DateTimeField(default=timezone.now, auto_now_add=True)
	text = models.TextField(blank=True)
	place_id = models.CharField(blank=True, max_length=255)
	shot = models.ForeignKey(Shot)

# vim: set ft=python ts=4 sw=4 :
