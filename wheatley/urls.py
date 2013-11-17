# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

from wheatley import views

urlpatterns = patterns('',
	# index
	url(r'^$', views.index, name='index'),
	# authentication
	url(r'^login/$', 'django.contrib.auth.views.login',
		kwargs={'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout',
		kwargs={'template_name': 'logout.html'}, name='logout'),
	# tweet
	url(r'^tweet/$', views.tweet, name='tweet'),
)

# vim: set ft=python ts=4 sw=4 :
