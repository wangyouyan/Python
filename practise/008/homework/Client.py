#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

"""
File Client codes
"""

import socket,time

HOST = '127.0.0.1'
PORT = 8009
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    cmd = raw_input('Please input command:').strip()
    if len(cmd) == 0:continue
    s.sendall(cmd)
    if cmd.split()[0] == 'get':
        with open(cmd.split()[1],'wb') as f:
            while True:
                data = s.recv(1024)
                if data == "FileTransferDone":
                    break
                f.write(s.recv(1024))
        continue
    else:
        print s.recv(1024)
s.close()