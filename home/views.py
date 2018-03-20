# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse , HttpResponseRedirect

from django.shortcuts import render,redirect
from .models import Post

def post_home(request):
    if(request.method == 'POST'):
        tit= request.POST['search']
        text="dhcvhsv"
        todo = Post(title=tit, text=text)
        todo.save()

        return redirect('/home')
    else:
    	context={
    	"title":"zomato",
    	}
        return render(request,'index.html',context)
