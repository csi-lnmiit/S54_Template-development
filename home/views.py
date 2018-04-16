from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse , HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from .models import *
from .forms import SignUpForm
from accounts.models import *
from review.models import Review,Comment
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

def get_user(request):
    if request.user.is_authenticated():
        user = request.user
        user_prof = UserProfile.objects.get(user_id=user)
        return user,user_prof
    else :
        user = None
        user_prof = None
        return user,user_prof

def search(request):
    if(request.method == 'POST'):
        c=0
        search = request.POST['search']
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
    else: return HttpResponseNotFound('<h1>Page not found</h1>')

def main(request):
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
    context= {}
    instance = Gym.objects.get(id=id)
    inst_add = (Address.objects.get(gym_id=id))
    com_add = inst_add.complete_add.split(";")
    inst_eq = Equipment.objects.filter(gym_id=id)
    inst_cont = Content_Long.objects.filter(gym_id=id)
    inst_pho = Photos.objects.filter(gym_id=id)
    nos=instance.contact.split(";")
    pac=instance.charges.split(";")
    timing = instance.timing.split(";")
    j=inst_pho.count()
    inst_review= Review.objects.filter(gym_id=id)
    inst_com= Comment.objects.filter(review_id__in=inst_review)
    print(inst_com)
    user,user_prof = get_user(request)
    if (user) :
        try:
            user_rev = Review.objects.get(gym_id=id,user_id=user)
        except ObjectDoesNotExist:
            user_rev = None 
    else : user_rev = None

    if ('review' in request.POST):
        if(user==None):
            error = "You must be logged in first to post a review"
            context.update({"error" : error})
        else:
            review = request.POST['review']
            # rating = request.POST['rating']
            p = Review.objects.create(gym_id=instance, user_id=user, content=review ,rating=4.0)
            p.save()
    elif ('comment'  in request.POST):
        if(user==None):
            error = "You must be logged in first to post a review"
            context.update({"error" : error})
        else:
            temp = request.POST['reviewid']
            r = Review.objects.get(gym_id=id,content=temp)
            comment = request.POST['comment']
            p = Comment.objects.create(review_id=r,user_id=user,comment=comment)
            p.save()
    context.update({
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
        "user" : user,
        "user_prof" : user_prof,
        "obj_review" : inst_review,
        "user_rev" : user_rev,
        "obj_comment" : inst_com,
    })
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
            password1 = userObj['password1']
            password2 = userObj['password2']
            email = userObj['email']
            first_name = userObj['first_name']
            last_name = userObj.get('last_name',None)
            age = userObj.get('age',None)
            img = userObj.get('profile-image',None)
            if (age <= 10):
                context = {
                    "message" : "Invalid Age",
                    "form" : form,
                }
            if (User.objects.filter(email=email).exists()):
                context = {
                    "message" : "Email already exists",
                    "form" : form,
                }
                return render(request, 'signup.html', context)
            if (password1 != password2):
                context = {
                    "message" : "Passwords didn't match",
                    "username" : username,
                    "form" : form,
                }
                return render(request, 'signup.html', context)
            if not (User.objects.filter(email=email).exists()):
                User.objects.create_user(email,first_name,password1)
                user = authenticate(email=email, password=password1)
                login(request, user)
                temp = UserProfile(user_id=user,last_name=last_name,age=age,prof_image=img)
                temp.save()
                return redirect('main')
            else :
                 raise forms.ValidationError('Looks like a username with that email and username already exists')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def contact(request):
    return render(request,'contact.html')