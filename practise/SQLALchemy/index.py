#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://otomat:otomat@localhost:3306/oldboy",max_overflow=5)

#engine.execute(
#    "insert into shopping_mall (ID,user,email,gender,cellphone,password,price) values(2,'wyy','wyy@che001.com','male',15611703075,'che001',1000)"
#)

#engine.execute(
#    "insert into shopping_mall (ID,user,email,gender,cellphone,password,price) values(%s,%s,%s,%s,%s,%s,%s)", ((11,'wyy','wyy@che001.com','male',15611703075,'che001',1000),(12,'wyy','wyy@che001.com','male',15611703075,'che001',1111),)
#)

result = engine.execute('select * from shopping_mall')
result.fetchall()
#for i in result.fetchall():
#    print i