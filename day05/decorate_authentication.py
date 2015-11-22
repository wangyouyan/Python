#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

def login(key):
    local = "ahhaahhahgsgsgs"
    if local == key:
        return True
    else:
        return False

def auth(func):
    def inner(*args,**kwargs):
        key = kwargs.pop('token')
        is_login = login(key)
        if not is_login:
            return '非法用户'
        temp = func(*args,**kwargs)
        print 'after'
        return temp
    return inner


@auth
def fetch_server_list(args):
    server_list = ['c1','c2','c3']
    return server_list

if __name__ == '__main__':
    print '-------------------'
    key = "ahhaahhahgsgsgs"
    ret_list = fetch_server_list('test',token=key)
    print ret_list