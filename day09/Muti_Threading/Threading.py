#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import threading
import time

def run(num):
    lock.acquire()
    global data
    print("thread....",num)
    data = -1
    lock.release()
    time.sleep(1)
lock = threading.Lock()
data = 100

for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()

print "---data---",data