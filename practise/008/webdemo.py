#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from wsgiref.simple_server import make_server

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    #对url(localhost:8001/dev)进行分割
    temp = url.split('/')[1]
    import home
    #去home模块儿中检查，是否含有指定的函数
    is_exist = hasattr(home, temp)
    #如果存在指定函数,
    if is_exist:
        #获取函数
        func = getattr(home, temp)
        #执行函数并获取返回值
        ret = func()
        #将函数返回值响应给请求看
        return ret
    else:
        return '404 not found'

if __name__ == '__main__':
    httpd = make_server('', 8001, RunServer)
    print "Serving HTTP on port 8001..."
    httpd.serve_forever()