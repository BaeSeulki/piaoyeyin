# coding=utf-8
from django.conf.urls import url
from . import views


app_name = 'blog'  # 指定命名空间
urlpatterns = [
    url(r'^$', views.index, name='index'),  # 网址，处理函数，处理函数的别名
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
