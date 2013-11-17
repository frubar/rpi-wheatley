# -*- coding: UTF-8 -*-

from django.contrib import admin

from wheatley.models import Photo, Location, Shot, Voice, Tweet

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_date', 'filename', 'encoding', 'effect',)
	search_fields = ('filename',)
	date_hierachy = ('created_date',)
	list_filter = ('created_date', 'encoding', 'effect',)
	list_display_link = ('id', 'filename',)

class LocationAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_date', 'description')
	search_fields = ('description',)
	date_hierachy = ('created_date',)
	list_filter = ('created_date',)
	list_display_link = ('id', 'description',)

class ShotAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_date', 'location', 'photo',)
	search_fields = ('location',)
	date_hierachy = ('created_date')
	list_filter = ('created_date',)
	list_display_link = ('id',)

class VoiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'text',)
	search_fields = ('text',)
	list_display_link = ('id',)

class TweetAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_date', 'shot',)
	date_hierachy = ('created_date',)
	list_filter = ('created_date',)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Shot, ShotAdmin)
admin.site.register(Voice, VoiceAdmin)
admin.site.register(Tweet, TweetAdmin)

# vim: set ft=python ts=4 sw=4 :
