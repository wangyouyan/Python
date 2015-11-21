#!/usr/bin/python
# -*- coding:utf-8 -*-

#print "Hello world"
"""
import sys
#捕获参数，并保存到集合
print sys.argv

# 字节码
import module
"""
#接收用户输入
"""
import getpass

name = raw_input("用户名:")
pwd = getpass.getpass("密码:")
if name == 'rain' and pwd == '123':
	print "登录成功"
else:
	print "用户名或密码不正确"
"""

import getpass

while 1:
	name = raw_input("用户名:")
	pwd = getpass.getpass("密码:") 
	if name == 'rain' and pwd == '123': 
		print "登录成功"
	elif name == 'alex' and pwd == '123':
		print "汽车之家"
	elif name == 'tony' and pwd == '123':
		print "好大夫在线"
	else:
		print "用户不存在..."
		break
	print "登录成功,当前用户为%s" % name
