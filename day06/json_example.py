#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import json
import datetime

name = {
    'alex':[22,"M",{1:{2:3}}],
    'rain':[22,"F"],
}
name_after_transfer = json.dumps(name)
f = file("data_to_qq.txt",'wb')
f.write(name_after_transfer)
