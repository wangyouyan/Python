#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

def Before(request,kargs):
    print 'before'

def After(request,kargs):
    print 'after'


def Filter(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):

            before_result = before_func(request,kargs)
            if(before_result != None):
                return before_result;

            main_result = main_func(request,kargs)
            if(main_result != None):
                return main_result;

            after_result = after_func(request,kargs)
            if(after_result != None):
                return after_result;

        return wrapper
    return outer

@Filter(Before, After)
def Index(request,kargs):
    print 'index'

Index('参数一','参数二')