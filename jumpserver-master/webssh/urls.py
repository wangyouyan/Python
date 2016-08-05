# coding:utf-8
from django.conf.urls import patterns, include, url
from webssh.views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r"get_auth_obj/",get_auth_obj,name="get_auth_obj"),
    url(r"host/connect/",host_connect,name="host_connect"),
)