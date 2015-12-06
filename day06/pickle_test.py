#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import pickle
import datetime

def sayHi():
    yield "test01"
    yield "test02"
    yield "test02"

t = sayHi()
print t.next(),type(t)
pickle