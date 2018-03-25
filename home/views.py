# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse , HttpResponseRedirect

from django.shortcuts import render,redirect
from .models import Gym

def main(request):
    queryset = Gym.objects.all()
    if(request.method == 'POST'):
        tit= request.POST['search']
        text="dhcvhsv"
        todo = Post(title=tit, text=text)
        todo.save()

        return redirect('/home')
    else:
    	context={
        "object_list" : queryset,
    	"title":"GYMS",
    	}
        return render(request,'index.html',context)

def detail(request):
    instance = Gym.objects.get()
    context = {
        "title = "
    }



def html_test(request):
    return render(request,'base.html')


