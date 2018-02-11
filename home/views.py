# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse , HttpResponseRedirect

from django.shortcuts import render

def post_home(request):
	context = {
	"title":"Zomato"
	}
	return render(request,"index.html",context)

# Create your views here.
