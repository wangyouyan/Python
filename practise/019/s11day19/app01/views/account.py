#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from django.shortcuts import render,render_to_response
from app01.forms import account as AccountForm

def login(request):
    obj = AccountForm.LoginForm(request.POST)
    if request.method == "POST":
        return render(request,'account/login.html',{'obj':obj})
    return render(request,'account/login.html',{'obj':obj})