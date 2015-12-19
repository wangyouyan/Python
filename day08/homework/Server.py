#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import time
import SocketServer
import commands

class   MyServer(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print "{} wrote:".format(self.client_address[0])
            if not self.data:
                print "client %s is dead!" % self.client_address[0]
                break
            user_input = self.data.split()
            if user_input[0] == 'get':
                with open(user_input[1],'rb') as f:
                    self.request.sendall(f.read())
                time.sleep(0.5)
                self.request.send('FileTransferDone')
                continue
            cmd_status,result = commands.getstatusoutput(self.data)
            if len(result.strip()) != 0:
                self.request.sendall(result)
            else:
                self.request.sendall('Done')

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()
    MyServer()
