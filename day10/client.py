#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import socket

ip_port = ('127.0.0.1',8888)
sk = socket.socket()
sk.connect(ip_port)
sk.setblocking(5)

while True:
    inp = raw_input('please input:')
    sk.sendall(inp)
    print sk.recv(1024)

sk.close()
