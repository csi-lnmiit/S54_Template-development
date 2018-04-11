from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse , HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from .models import *
from .forms import SignUpForm
from django.contrib.auth.models import User
from django import forms



def main(request):
    if(request.method == 'POST'):
        c=0
        search= request.POST['search']
        todo_list = Gym.objects.filter(title__icontains=search)
        if(todo_list):
            paginator = Paginator(todo_list , 4) # Show 25 contacts per page
            page = request.GET.get('page')
            try:
                todo = paginator.page(page)
            except PageNotAnInteger:
                todo = paginator.page(1)
            except EmptyPage:
                todo = paginator.page(paginator.num_pages)
            context = {
            "object_list" : todo,
            "title" : "Search Result of " + search,
            "search" : search,
            "page": page,
            }
        else:
            context = {
            "title" : "Search Result of " + search,
            "search" : search,
            "c" : c+1
            }
        return render(request,'search.html',context)
    else:
        queryset_list = Gym.objects.all()
        paginator = Paginator(queryset_list, 4) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    	context={
        "object_list" : queryset,
    	"title":"GYMS",
        "page": page,
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
    j=0
    for p in inst_pho:
        j+=1
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
        "j" : j,

    } 
    print context
    return render(request,'details.html',context)

def photo(request,id=id):
    inst_pho = Photos.objects.filter(gym_id=id)    
    context = {
        "obj_photos" : inst_pho,
        } 
    return render(request,'photos.html',context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password1 = userObj['password1']
            password2 = userObj['password2']
            email = userObj['email']
            if (password1 != password2):
                context = {
                    "mesaage" : "Passwords didn't match",
                    "username" : username,
                    "form" : form,
                }
                return render(request, 'signup.html', context)
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password1)
                user = authenticate(username=username, password=password1)
                login(request, user)
                return redirect('main')
            else :
                 raise forms.ValidationError('Looks like a username with that email and username already exists')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    

    
def html_test(request):
    return render(request,'base.html')