#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

'''
obj = file('文件路径','')
obj = open('文件路径','')  #推荐是用open的方式打开文件
'''

obj = open('./history.txt','r+')  #r,w,a
obj.seek(15)   #字符的起始值
obj.truncate() #截断数据,根据当前指针位置截断
print   obj.read()
print   obj.tell()  #查看指针位置
obj.close()
#obj.seek()
#obj.tell() 读文件过程中的指针
