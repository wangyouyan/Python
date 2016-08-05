#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

def get_user():
    #obj = SqlHelper()
    obj = SqlHelper.instance()
    obj.fetch()
    print id(obj)
    return '1'

def del_user():
    #obj = SqlHelper()
    obj = SqlHelper.instance()
    obj.remove()
    return '1'