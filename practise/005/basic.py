#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

#创建一个装饰器函数,无参数
def auth(func):
    def inner():
       # print "before....."
        func()
       # print "after....."
    return inner

#有一个参数的装饰器函数
def auth_arg(func):
    def inner(arg):
        print 'before....'
        func(arg)
        print 'after'
    return inner

#创建一个动态参数的装饰器函数
def auth_args(func):
    def inner(*args,**kwargs):
     #   print "Before......"
        func(*args,**kwargs)
      #  print "after......"
    return inner


#函数1
@auth
def f1():
    print "f1"

#函数2
@auth
def f2():
    print "f2"

#函数3
@auth_arg
def f3(arg):
    print 'f3',arg

@auth_args
def f4():
    print 'f4'

@auth_args
def f5(args):
    print 'f5',args

@auth_args
def f6(*args,**kwargs):
    print 'f6','f7',args,kwargs

if __name__ == '__main__':
#    f1()
#    print "-----------"
#    f2()
#    f3('1.2.3.4.5')
    f4()
    f5('Hello,f5')
    f6('welcome','oldboy')
