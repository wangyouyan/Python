#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

#创建一个装饰器函数
def auth(func): #func = f1 ==> func()<==>f1()
    def inner():
        print "This is a inner function"
        func()  #f1==>原函数
    return inner
def f1():
    print 'f1'
'''
ret = auth(f1) = def inner():
                    print "This is a inner function"
                    func()  #f1==>原函数
                return inner
'''
#函数1
@auth
def f1():
    print "f1 函数"

#函数2
def f2():
    print "f2 函数"

