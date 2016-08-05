#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

'''
Python递归
0，1，1，2，3，5，8，
13，21，34，55，89，144，233，377，610，987
'''

#打印如上所述数列,前两个数相加
def func(arg1,arg2):
    if arg1 == 0:
        pass
    arg3 = arg1 + arg2
    if arg3>1000:
        return arg3
    ret = func(arg2,arg3)
    print ret
result = func(0,1)
print result