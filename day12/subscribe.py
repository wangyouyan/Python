#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from monitor.RedisHelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg= redis_sub.parse_response()
    print msg