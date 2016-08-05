#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^login/$',views.login),
    url(r'^home/$',views.home),
    #url(r'^user_list/(\d+)/(\d+)$',views.user_list),
    #url(r'^user_list/(?P<v1>\d+)/(?P<v2>\d+)$',view.user_list),
    #url(r'^$',views.index),
]
