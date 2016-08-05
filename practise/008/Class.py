#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

class Foo:
    static_name = 'nba'
    def __init__(self):
        self.name = 'alex'

    def show(self):
        pass

    @staticmethod
    def static_show():
        pass

    @classmethod
    def class_show(cls):
        pass

obj = Foo()
print obj.__dict__
print hasattr(obj,'name')
print hasattr(obj,'show')
