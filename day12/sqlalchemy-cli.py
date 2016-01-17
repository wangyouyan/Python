#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from sqlalchemy import create_engine
import threading

#database connection pool
engine = create_engine("mysql+mysqldb://otomat:otomat@localhost:3306/oldboy",pool_size=5,max_overflow=5)

#engine.execute(
#    "INSERT INTO shopping_mall(user,email) VALUES('RainWang','20160117')"
#)

def func(i):
    conn = engine.connect()
    conn.execute("select * from shopping_mall")
    import time
    time.sleep(10)
    print i
    conn.close()

for i in range(30):
    t = threading.Thread(target=func,args=(i,))
    t.start()