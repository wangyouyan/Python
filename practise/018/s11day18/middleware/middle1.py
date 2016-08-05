#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from django.shortcuts import HttpResponse

class mmm(object):
    def process_request(self,request):
        print "mmm.process_request"
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print "mmm.process_view"
    def process_reponse(self,request,response):
        print "mmm.process_reponse"
        return response

class xxx(object):
    def process_request(self,request):
        print "xxx.process_request"
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print "xxx.process_view"
    def process_reponse(self,request,response):
        print "xxx.process_reponse"
        return response
