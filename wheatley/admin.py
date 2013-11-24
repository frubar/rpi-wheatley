# -*- coding: UTF-8 -*-

from django.contrib import admin

from wheatley.models import Photo, Location, Tweet, Settings

class SettingsAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_at',)
	list_display_links = ('id', 'created_at',)
	date_hierachy = ('created_at',)
	list_filter = ('created_at',)


class PhotoAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_at', 'filename', 'location',)
	list_display_links = ('id', 'filename')
	date_hierachy = ('created_at',)
	list_filter = ('created_at', 'location',)

class LocationAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_at', 'title',)
	list_display_links = ('id', 'title',)
	date_hierachy = ('created_at',)
	list_filter = ('created_at',)
	search_fields = ('title',)

class TweetAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_at', '__unicode__', 'location',)
	list_display_links = ('id', '__unicode__')
	date_hierachy = ('created_at',)
	list_filter = ('created_at', 'location',)

admin.site.register(Settings, SettingsAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Tweet, TweetAdmin)

# vim: set ft=python ts=4 sw=4 :
