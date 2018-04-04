# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse , HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from .models import *

def main(request):
    queryset = Gym.objects.all()
    paginator = Paginator(queryset, 4) # Show 25 contacts per page
    page_request_var="page"
    page = request.GET.get('page_request_var')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
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
        "page_request_var": page_request_var,
    	}
        return render(request,'index.html',context)

def detail(request,id=id):
    instance = Gym.objects.get(id=id)
    inst_add = (Address.objects.get(gym_id=id))
    com_add = inst_add.complete_add.split(";")
    inst_eq = Equipment.objects.filter(gym_id=id)
    inst_cont = Content_Long.objects.filter(gym_id=id)
    inst_pho = Photos.objects.filter(gym_id=id)
    nos=instance.contact.split(";")
    pac=instance.charges.split(";")
    timing = instance.timing.split(";")
    context = {
        "title" : instance.title,
        "object" : instance,
        "obj_add" : inst_add,
        "obj_content" : inst_cont,
        "obj_equip" : inst_eq,
        "obj_photos" : inst_pho,
        "com_add" : com_add,
        "nos" : nos,
        "pac" : pac,
        "timing" : timing,
    }
    print context
    #print obj_equip
    return render(request,'details.html',context)


def html_test(request):
    return render(request,'base.html')


