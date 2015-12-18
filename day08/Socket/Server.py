#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import socket


host=('localhost',8341)
objserver = socket.socket()
objserver.bind(host)
objserver.listen(5)

while True:
    print "waiting......"
    conn,addr = objserver.accept()
    #最多接受的size
    client_data = conn.recv(1024)
    print client_data
    conn.send('This is server from %s' % host[0])
    conn.close()
