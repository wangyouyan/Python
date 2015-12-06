#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import json

f = file('data_to_qq.txt','rb')
name = json.loads(f.read())
f.close()
print name["alex"]