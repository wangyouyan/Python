#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import smtplib,string

HOST = "smtp.163.com"   #定义smtp主机
SUBJECT = "Test email from Python" #定义邮件主题
TO = "testmail@qq.com"  #定义邮件收件人
FROM = "jumpserver001@163.com"  #定义邮件发件人
text = "Python rules them all"  #邮件内容

BODY = string.join((
    "From: %s"  % FROM,
    "To: %s"    % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
),"\r\n")

server = smtplib.SMTP() #创建一个SMTP()对象
server.connect(HOST,"25")   #通过connect方法连接smtp主机
server.starttls()   #启动安全传输模式
server.login("jumpserver001@163.com","OpenStack2015")   #邮箱账号登录校验
server.sendmail(FROM,[TO],BODY) #邮件发送
server.quit()   #断开smtp连接

