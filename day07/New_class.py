#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

'''
当类是经典类时，多继承情况下，会按照深度优先方式查找
当类是新式类时，多继承情况下，会按照广度优先方式查找
'''

class D:
    def bar(self):
        print 'D.bar'

class C(D):
    def bar(self):
        print 'C.bar'

class B(D):
    pass

class A(B,C):
    pass

a = A()
a.bar()