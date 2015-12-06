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

GRANT ALL PRIVILEGES ON *.* TO 'otomat'@'localhost' IDENTIFIED BY 'che001' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'otomat'@'%' IDENTIFIED BY 'che001' WITH GRANT OPTION;