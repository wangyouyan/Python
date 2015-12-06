#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import os,sys
import hmac
import getpass
sys.path.append("/Users/Rain/Python/practise/modules")
import MySQL
dbconn = MySQL.DBconnection()



def register():
    print('欢迎注册天猫超市!')
    username=raw_input('用户名:').strip()
    email=raw_input('邮箱:').strip()
    gender=raw_input('性别:').strip()
    cellphone=raw_input('手机号:').strip()
    password=getpass.getpass('密码:').strip()
    price=raw_input('价格:').strip()
#    print username,email,gender,cellphone,password
    #将注册信息插入到数据库中
    conn = dbconn.cursor()
    conn.execute("insert into shopping_mall values(10,%s,%s,%s,%s,%s,%s) % (username,email,gender,cellphone,password,price)")
if __name__ == '__main__':
    register()



