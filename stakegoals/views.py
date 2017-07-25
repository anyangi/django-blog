# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.


def home(request):
	posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'post_list.html',{'posts':posts})

#@login_required
def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'post_detail.html',{'post':post})

