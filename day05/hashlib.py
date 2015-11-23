#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com


import md5
hash = md5.new()
hash.update('admin')
print hash.hexdigest()

"""

import hashlib

hash = hashlib.md5('wyyservice')
hash.update('admin')

print hash.hexdigest() """

import hmac

