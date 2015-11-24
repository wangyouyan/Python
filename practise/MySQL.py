#!/usr/bin/env python
#-*- coding: utf-8 -*

import MysqlDBConn

dbconn = MysqlDBConn.DBConn()

def process():
    dbconn.connect()
    dropTable()
    createTable()
    insertDatas()
    #insertData()
    #updateData()
    #queryData()
    #dbconn.close()

def dropTable():
    '''delete tables '''
    conn=dbconn.cursor()
    conn.execute('''DROP TABLE IF EXISTS `lifeba_users`''')

def createTable():
    conn=dbconn.cursor()
    conn.execute('''CREATE TABLE `lifeba_users` (
    `ID` int(11) NOT NULL auto_increment,
    `name` varchar(50) default NULL,
    `realName` varchar(50) default NULL,
    `age` int(11) default NULL,
    PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
''')

def insertData():
    sql = "insert into lifeba_users(name,realname,age) values('%s','%s','%s')" % ("rain","test","28")
    print sql
    execute(sql)

def insertDatas():
    sql = "insert into lifeba_users(name,realname,age) values('%s','%s','%s')" 
    tmp = (('alex','test02',30),('peiqi','test03',27))
    executemany(sql,tmp)

def updateData():
    sql = "update lifeba_users set realname = '%s' where name='rain' " % "modify"
    execute(sql)

def queryData():
    sql = "select * from lifeba_users"
    rows = query(sql)
    printResult(rows)

def deleteData():
    sql = "delete from lifeba_users where id=2"
    execute(sql)

def executemany(sql,tmp):
    conn=dbconn.cursor()
    conn.executemany(sql,tmp)

def execute(sql):
    conn=dbconn.cursor()
    conn.execute(sql)

def query():
    conn=dbconn.cursor()
    conn.execute(sql)
    rows = conn.fetchmany(10)
    return rows

def printResult(rows):
    for row in rows:
        for i in range(0,len(row)):
            print row[i]
        print ''

if __name__ == '__main__':
    process()
