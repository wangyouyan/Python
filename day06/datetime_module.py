#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import datetime

time = datetime.datetime.now()
time.strftime("%Y-%m-%d %H:%S")
t = time.strptime("2015-9-19 19:33","%Y-%m-%d %H:%S")
time.mktime(t)

datetime.datetime.now() + datetime.timedelta(minutes=10)