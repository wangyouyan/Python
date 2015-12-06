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


'''
conn=MySQLdb.connect(host='localhost',port=3306,user='otomat',passwd='OpenStack001',db='oldboy',charset='utf8')
cur = conn.cursor()
cur.execute("select user from shopping_mall;")
user=cur.fetchone()
cur.execute("insert into shopping_mall values(5,'tom','tom@che001.com','male','15611703075','che001','1314')")
sqli="insert into shopping_mall values(%s,%s,%s,%s,%s,%s,%s)"
cur.executemany(sqli,[(6,'sam','tom@che001.com','male','15611703075','che001','1314'),(7,'som','tom@che001.com','male','15611703075','che001','1314'),])
cur.commit()
cur.close()
'''
