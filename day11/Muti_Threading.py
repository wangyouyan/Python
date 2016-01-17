#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import contextlib
import threading
import time
import random

doing = []
def num(l2):
    while True:
        print len(l2)
        time.sleep(1)
t = threading.Thread(target=num,args=(doing,))
t.start()

@contextlib.contextmanager
def show(l1,item):
    doing.append(item)
    yield
    doing.remove(item)

def task(i):
    flag = threading.current_thread()
    with show(doing,flag):
        time.sleep(random.randint(1,4))

for i in range(20):
    temp = threading.Thread(target=task,args=(i,))
    temp.start()



