#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import paramiko
import os,sys,time

blip = "127.0.0.1"    #定义堡垒机信息
bluser = "root"
blpasswd = "che001"

hostname = "127.0.0.1"  #定义业务服务器信息
username = "root"
password = "che001"

tmpdir = "/tmp"
remotedir = "/data"
localpath = "/home/nginx_access.tar.gz"     #本地源文件路径
tmppath = tmpdir+"/nginx_access.tar.gz"      #堡垒机临时路径
remotepath = remotedir+"/nginx_access_hd.tar.gz"        #业务主机目标路径
port = 22
passinfo='\' password: '
paramiko.util.log_to_file('syslogin.log')
t = paramiko.Transport(blip,port)
t.connect(username=bluser,password=blpasswd)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath,tmppath)     #上传本地源文件到堡垒机临时路径
sftp.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpasswd)

channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''
#scp中转目录文件到目标主机
channel.send('scp '+tmppath+' '+username+'@'+hostname+':'+remotepath+'\n')
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception,e:
        print 'Error info:%s connection time.'  % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no')==-1:
        channel.send('yes\n')
        buff=''

channel.send(password+'\n')

buff=''
while not buff.endswith('# '):
    resp = channel.recv(9999)
    if not resp.find(passinfo)==-1:
        print 'Error info: Authentication failed.'
        channel.close()
        ssh.close()
        sys.exit()

    buff += resp
print buff
channel.close()
ssh.close()

