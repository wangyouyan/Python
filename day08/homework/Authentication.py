#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import os,sys

class Register(object):
    username = raw_input('用户名:')
    pwd = raw_input('密码:')
    cellphone = raw_input('手机号:')
    email = raw_input('邮箱:')
    if len(username.strip()) == 0:
        print("用户名不能为空")
        sys.exit(0)
    elif len(pwd.strip()) == 0:
        print("密码不能为空")
        sys.exit(0)
    else:
        f = open('./database.txt','r+')
        info = "%s %s %s %s" % (username,pwd,cellphone,email)
        f.write(info)
        f.write('\n')
        #f.write("%s-%s-%s-%s \t") % (username,pwd,cellphone,email)
        f.close()
"""
class Login(object):
    user = Register.username
    passwd = Register.pwd
    if user == raw_input('用户名:') and passwd == getpass.getpass('密码:'):
        print('登录成功!')
    else:
        print('用户名和密码错误!')
"""
if __name__ == '__main__':
    Register()

