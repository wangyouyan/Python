#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import sys
sys.path.append('/Users/Rain/Python/practise/modules/')
import MySQL

dbconn = MySQL.DBconnection()

def execute(sql):
    conn=dbconn.cursor()
    conn.execute(sql)

if __name__ == '__main__':
    sql="show databases;"
    execute(sql)