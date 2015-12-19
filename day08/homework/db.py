#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import MySQLdb

class DBconnection:
    conn = None
    def connect(self):
        self.conn = MySQLdb.connect(host='localhost',port=3306,user='otomat',passwd='OpenStack001',db='oldboy',charset='utf8')

    def cursor(self):
        try:
            return self.conn.cursor()
        except(ArithmeticError,MySQLdb.OperationalError):
            print self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.close()