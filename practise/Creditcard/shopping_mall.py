#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import os,sys,time

def mall():
    shopping_list = []
    flag = True
    init = 0
    print "欢迎来到天猫商城"
    print '''商品清单:
            1. iphone 2188$
            2. ipad  3552$
            3. nexus 1999$
            4. meizu 1520$
            5. meide 1000$
            6. iwatch 3565$
        '''
    shopping_dict = {
        'iphone':2188,
        'ipad':3552,
        'nexus':1999,
        'meizu':1520,
        'meide':1000,
        'iwatch':3565,
        'quit':0
    }
    while flag:
        cart=raw_input("请将喜欢的商品加入购物车:")
        price = shopping_dict[cart]
        init += price
        print init
        if price == 0:
            break