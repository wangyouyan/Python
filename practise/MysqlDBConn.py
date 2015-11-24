#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb

class DBConn:
    conn = None
    def connect(self):
        self.conn = MySQLdb.connect(host='localhost',port=3306,user='otomat',passwd='che001',db='otomat',charset='utf8')

    def cursor(self):
        try:
            return self.conn.cursor()
        except(ArithmeticError,MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.close()