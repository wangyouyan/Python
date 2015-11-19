#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

'''
实现堡垒机模式下的远程命令执行
'''

import paramiko
import os,sys,time

ip = "127.0.0.1" #定义堡垒机信息
user = "rain"
password = "che001"

hostname = "127.0.0.1"  #定义业务服务器信息
username = "rain"
passwd  = "che001"

port = 22
passinfo = '\' password: '  #传入服务器密码的前标志串
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()  #ssh登录堡垒机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip,username=user,password=password)

channel=ssh.invoke_shell()  #创建会话，开启命令调用
channel.settimeout(10)  #会话命令执行超时时间，单位为秒

buff = ''
resp = ''
channel.send('ssh '+username+'@'+hostname+'\n') #执行ssh登录业务主机
while not buff.endswith(passinfo):  #ssh登录的提示信息判断，输出串尾含有"\'s password:" 时退出while循环
    try:
        resp = channel.recv(9999)
    except Exception,e:
        print 'Error info:%s    connection time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no')==-1:     #输出串尾含有"yes/no"时发送"yes"并回车
        channel.send('yes\n')
        buff=''

channel.send(password+'yes\n')      #发送业务主机密码

buff =''
while not buff.endswith('# '):   #输出串尾为"#"时说明校验通过并退出while循环
    resp = channel.recv(9999)
    if not resp.find(passinfo)==-1:     #输出串尾含有"\'s password: " 时说明密码不正确,要求重新输入
        print 'Error info:  Authentication failed.'     #关闭连接对象后退出
        channel.close()
        sys.exit()
    buff += resp

channel.send('ifconfig\n')  #认证通过后发送ifconfig命令来查看结果
buff=''
try:
    while buff.find('# ')==-1:
        resp = channel.recv(9999)
        buff += resp
except  Exception, e:
    print "error info:"+str(e)

print buff      #打印输出串
channel.close()
ssh.close()

