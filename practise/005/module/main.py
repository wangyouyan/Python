#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

#实现某功能，且是实现的所有代码的集合
#模块儿有两种存在方式:.py  "文件夹"
#模块儿:1>自己写的模块儿；2>别人写的模块儿.

import MySQL
import sys
sys.path.append('/Users/Rain/Python/')  #添加模块儿的环境变量
sys.path.append('/Users/Rain/Python/day05/')
import module
import django
sys.argv
from sys import argv
from MySQL import argv as test



if __name__=='__main__':
    MySQL.connection()
    MySQL.argv()
    print django.get_version()
    module.test()