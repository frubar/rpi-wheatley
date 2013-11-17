# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html')

@login_required(login_url='login')
def tweet(request):
	return render(request, 'tweet.html')

# vim: set ft=python ts=4 sw=4 :
