#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

'''
class Person(object):
    def __init__(self,name): #初始化函数
        self.name = name
    #    print "------>create:",name

    def say_name(self):
        print "My name is %s" % self.name

p1 = Person("oldboy01") #实例化
p2 = Person("oldboy02") #实例化

p1.say_name()
p2.say_name()


print p1,p2
'''


class Myclass(object):
    def __init__(self,province,City):
        self.province = province
        self.City = City

    def city(self):
        print "This is the capital of %s-%s" % (self.province,self.City)

    def sence(self):
        print self.City

name1 = Myclass("湖北省","武汉市")
name2 = Myclass("福建省","福州市")

name1.city()
name2.city()
print("\t")
name2.sence()