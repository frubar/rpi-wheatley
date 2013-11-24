# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

from wheatley import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
)


# vim: set ft=python ts=4 sw=4 :
