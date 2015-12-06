#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

class Province(object):
    country = '中国'

    def __init__(self,name):
        self.name = name

shanxi = Province("山西")
print id(shanxi.country)
shandong = Province("山东")
print id(shandong.country)
henan = Province("河南")

#普通字段
print shandong.name
print shanxi.name

#静态字段
print Province.country
