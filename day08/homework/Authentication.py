#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

class Register(object):
    username = raw_input('用户名:')
    pwd = raw_input('密码:')
    cellphone = raw_input('手机号:')
    email = raw_input('邮箱:')
    if len(username.strip()) != 0:
        print "有效的用户",len(username.strip())
    else:
        print "无效的用户"

class Login(object):
    pass

