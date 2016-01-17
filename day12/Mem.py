#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import memcache


mc = memcache.Client(['10.211.55.4:12000'], debug=True)
mc.set("foo", "bar")
ret = mc.get('foo')
print ret
