#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import socket
import select

#
ip_port = ('127.0.0.1',8888)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
sk.setblocking(False)

inputs = [sk]
'''while True:
    rList,w,e = select.select(inputs,[],[],0.05)
    import time
    time.sleep(2)
    print 'input',inputs
    print 'result',rList
    for r in rList:
        if r == sk:
            conn,address == r.accept()
            inputs.append(conn)
            print address
        else:
            client_data = r.recv(1024)
            r.sendall(client_data)
            '''

while True:
    rList,wList,e = select.select(inputs,output,inputs,1)
    for r in rList:
        if r == sk:
            conn,address = r.accept()
            inputs.append(conn)
        else:
            client_data = r.recv(2014)
            if client_data:
                output.append(r)

    for w in wList:
        w.sendall('123')
        output.remote(w)



