# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
# index 页面
def index(request):
    # 列出所有的Post内容，'-'表示逆序
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        # 可以传入参数到html
        'welcome': '欢迎来到!',
        'title': '飘叶音的首页',
        'post_list': post_list
    })


# detail 页面
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})