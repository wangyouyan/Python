#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import select

import Queue
#
ip_port = ('127.0.0.1',8888)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
sk.setblocking(False)

inputs = [sk]
output = []
message = {}
#message = {
#    'c1':队列，
#    'c2':队列，【b,bb,bbb】
#}
while True:
    rList,wList,e = select.select(inputs, output, inputs, 1)
    # 文件描述符可读，rList，一，只有变化，感知
    # 文件描述符可写，wList，二，只有有，感知
    for r in rList:
        if r == sk:
            conn,address = r.accept()
            inputs.append(conn)
            message[conn] = Queue.Queue()
        else:
            client_data = r.recv(1024)
            if client_data:
                # 获取数据
                output.append(r)
                # 在指定队列中插入数据
                message[r].put(client_data)
            else:
                inputs.remove(r)
    for w in wList:
        # 去指定队列取数据
        try:
            data = message[w].get_nowait()
            w.sendall(data)
        except Queue.Empty:
            pass
        output.remove(w)
        del message[w]