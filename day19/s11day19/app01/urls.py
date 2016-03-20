from django.conf.urls import url,include
from django.contrib import admin
from app01.views import account,home

urlpatterns = [
    url(r'^login/',account.login),
    url(r'^index/',home.index),
]
