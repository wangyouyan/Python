#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import os,sys
import pickle
import json
import hmac
import getpass

def login():
    num = hmac.new('openstack')
    num.update('6222020200076156252')
    passwd = hmac.new('che001')
    passwd.update('123456')
    cardNum = raw_input('卡号:')
    cardnum = hmac.new('openstack')
    cardnum.update(cardNum)
    password = getpass.getpass('密码:')
    pwd = hmac.new('che001')
    pwd.update(password)
    if cardnum.digest() == num.digest() and pwd.digest() == passwd.digest():
        print('欢迎登录中国工商银行信用卡中心')
    else:
        print('无效的密码')

if __name__ == '__main__':
    login()
