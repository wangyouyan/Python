#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from django.shortcuts import render
from app01.forms import home as HomeForm
from app01 import models

def index(request):
    models.UserInfo.objects.all().delete()
    models.UserInfo.objects.create(name='Rain')
    after_list = models.UserInfo.objects.all()
    print after_list[0].ctime

    obj = HomeForm.ImportForm()
    return render(request,'home/index.html',{'obj':obj})