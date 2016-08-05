#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import socket

host=('localhost',8341)
obj = socket.socket()
obj.connect(host)
obj.send('请占领地球......')
server_data = obj.recv(1024)
print server_data
obj.close()
