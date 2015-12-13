#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

"""
import controller == import "home"
import home
import home as hh
import home as module
"""

controller,action = raw_input('url:').split('/')
module = __import__(controller)
is_exist = hasattr(module,action)
if is_exist:
    func = getattr(module,action)
    ret = func()
    print ret
else:
    print '404 not found'
