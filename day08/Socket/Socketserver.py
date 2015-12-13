#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import SocketServer
import os

class MyServer(SocketServer.BaseRequestHandler):

    def handle(self):
        print "got connection from",self.client_address
        while True:
            data = self.request.recv(1024)
            print "Recv from cmd:%s" % data

            cmd_res = os.popen(data).read()
            print 'cmd_res:',len(cmd_res)
            self.request.send(str(len(cmd_res)))
            self.request.recv(1024)
            self.request.sendall(cmd_res)

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()
    MyServer()