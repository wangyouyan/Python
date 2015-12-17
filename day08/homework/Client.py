#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import socket

ip_port = ('10.10.1.225','8009')
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(10)

while True:
    inp = raw_input('Please input command:')
    sk.sendall(inp)
    res_size = sk.recv(1024)
    print "Received the data size:",res_size,type(res_size)
    total_size = 0
    while True:
        data = sk.recv(1024)
        received_size += len(data)
        print('---------data-----------')
        if total_size == received_size:
            print data
            print('------data-----')
            break
        print data
        if inp == 'exit':
            break
    sk.close()