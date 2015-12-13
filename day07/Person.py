#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

class Person(object):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def func(self):
        return "123"

    @property   #把一个方法伪造成一个字段，在调用的时候不用输入括号().
    def att(self):
        return "123"

#类成员
obj = Person('Rain',2)


obj.name
obj.func()
obj.att

