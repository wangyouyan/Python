#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

"""
import socket

obj = socket.socket()
obj.connect(('localhost',8009))
#返回服务器IP地址和端口
print obj.getpeername()
obj.send('0000000')
server_data = obj.recv(1024)
print server_data
obj.close()
"""

import socket

ip_port = ('127.0.0.1',8009)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    inp = raw_input('please input:')
    sk.sendall(inp)
    res_size = sk.recv(1024)
    print "going to recv data size:",res_size,type(res_size)
    total_size = int(res_size)
    received_size = 0
    while True:
        data = sk.recv(1024)
        received_size += len(data)
        print '-----data-----'
        if total_size == received_size:
            print data
            print('-----not data------')
            break
        print data
        if inp == 'exit':
            break

    sk.close()