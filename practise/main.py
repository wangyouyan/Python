#!/usr/bin/env python
#-*- coding: utf-8 -*

import os,sys
import time
import getpass
import hmac

def login():
    #Creditcard encryption
    cardnum = hmac.new('openstack')
    cardnum.update('6222020200076156252')
    user_input = raw_input('CreditcadNum:')
    encryption_cardnum = hmac.new('openstack')
    encryption_cardnum.update(user_input)
    #Creditcard authtication password
    pwd = hmac.new('che001')
    pwd.update('123456')
    user_pwd = getpass.getpass('CreditcardPwd:')
    encryption_password = hmac.new('che001')
    encryption_password.update(user_pwd)
    #Verify if the cardnum or password is correct
    if cardnum.digest() == encryption_cardnum.digest() and pwd.digest() == encryption_password.digest():
        print('欢迎登录中国工商银行信用卡中心')
    else:
        print('无效的密码')
