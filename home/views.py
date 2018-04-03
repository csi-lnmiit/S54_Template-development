# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse , HttpResponseRedirect

from django.shortcuts import render,redirect
from .models import *

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

def detail(request,id=id):
    instance = Gym.objects.get(id=id)
    inst_add = (Address.objects.get(gym_id=id))
    com_add = inst_add.complete_add.split(";")
    inst_eq = Equipment.objects.filter(gym_id=id)
    inst_cont = Content_Long.objects.filter(gym_id=id)
    inst_pho = Photos.objects.filter(gym_id=id)
    nos=instance.contact.split(";")
    pac=instance.charges.split(";")
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
    }
    print context
    #print obj_equip
    return render(request,'details.html',context)


def html_test(request):
    return render(request,'base.html')


