# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
	post = Post.objects.all()
	return render(request,'blog.html',{'post':post})
