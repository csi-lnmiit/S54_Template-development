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
        return render(request,'base.html',context)
# def post_list(request):
#     # if request.user.is_authenticated():
#     #   context={
#     #       "title": "my list"
#     #   }
#     # else:
#     #   context={
#     #       "title": "list"
#     #   }
#     queryset_list=Post.objects.all()#.order_by("-timestamp")
#     paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
#     page_request_var="page"
#     page = request.GET.get('page_request_var')
#     try:
#         queryset = paginator.page(page)
#     except PageNotAnInteger:
#         queryset = paginator.page(1)
#     except EmptyPage:
#         queryset = paginator.page(paginator.num_pages)

#     context={
#             "object_list": queryset,
#             "title": "my list",
#             "page_request_var": page_request_var
#             }
#     #return render(request,"base.html",context)
#     return render(request,"post_list.html",context)