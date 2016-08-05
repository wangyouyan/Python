#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import re

#re.match
#re.search
print re.findall("^\d+]","abc123def456ghj*sdf3_abd")
print re.split("[\d,\*]","a,bc123def456ghj*sdf3_abd")
print re.sub("ab","YUE","abc123def456ghj*sdf3_abd",count=1)
#re.match("abc","abcdefg")

t = "int addr:10.43.0.22 Bcast:10.43.0.255 Mask:255.255.255.0"
print re.search("(\d+\.){3}(\d+)",t).group()

#匹配IP地址
str2 = "int addr:192.12.0.22 Bcast:10.43.0.255 Mask:255.255.255.0"
ip = re.search("([0-2]{0,1}[0-9]{0,1}[0-9]{0,3}.){3}([0-9]{1,3}[0-9]{0,3}[0-9]{0,3})",str2) #IP
print ip
name = "Rain Wang"
res = re.search("(?P<name>\w+)\s(?P<last_name>\w+)",name)
print res
