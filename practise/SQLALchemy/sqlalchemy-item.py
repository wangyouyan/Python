#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://otomat:otomat@localhost:3306/oldboy",max_overflow=5)

#事物操作
with engine.begin() as conn:
    conn.execute("insert into oldboy (id,lastname,firstname,age) values (1,'Rain','Wang',26)")
#    conn.execute("my_special_procedure(5)")

conn = engine.connect()

#事物操作
#with conn.begin():
#       conn.execute("some statement", {'x':5, 'y':10})

