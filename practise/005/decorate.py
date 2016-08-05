#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

def auth(func):
    def inner(*args,**kwargs):
        print 'before'
        #func代指fetch_server_list 原函数
        temp = func(*args,**kwargs)
        print 'after'
        return temp
    return inner

@auth
def fetch_server_list(args):
    server_list = ['c1','c2','c3']
    return server_list


if __name__ == '__main__':
    print '==================='
    ret_list = fetch_server_list('test')
    print ret_list
