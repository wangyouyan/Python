#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

class Person(object):
    """
    This is a document
    """
    def __init__(self):
        print "alex"
    def __call__(self, *args, **kwargs):
        print "call"

obj = Person()()
print obj.__doc__
