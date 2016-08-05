#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import threading
import sys
import socket
import select

ip_port = ('127.0.0.1',8888)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
sk.setblocking(False)

sk1 = socket.socket()
sk1.bind(('127.0.0.1',9999))
sk1.listen(5)
sk1.setblocking(False)

while True:
    '''
    readable,writeable,error = select.select([sys.stdin,],[],[])
    if sys.stdin in readable:
        print 'select get stdin',sys.stdin.readline()
    '''
    rlist,w,e = select.select([sk,sk1],[],[],2)
    for r in rlist:
        con,address = r.accept()
        print address