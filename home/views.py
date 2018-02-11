# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse , HttpResponseRedirect

from django.shortcuts import render

def post_home(request):
	return HttpResponse("<h1>Hello guys</h1>")

# Create your views here.
