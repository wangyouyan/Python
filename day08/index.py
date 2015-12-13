#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com
'''
import home

print "Welcome to Oldboy....."

url = raw_input('url:')

if url == 'home/dev':
    ret = home.dev()
    #print ret

elif url == 'home/index':
    ret = home.index()
    #print ret

else:
    print '404.html'

controller,action = url.split('/')

func = getattr(home,action)

ret = func()
print ret
'''
#以下4个函数所含的方法
#找到home文件,内容加载到内存
import home
#print dir(home)
#print hasattr(home,'deasafasdfaa')
#print getattr(home,'dev')

#setattr(home,'alex',lambda x:x+1)
#print dir(home)

delattr(home,'dev')
print dir(home)

'''
//操作内存中某个容器的元素
//四个函数分别用于对对象内部执行：检查是否含有某成员、获取成员、设置成员、删除成员。
getattr()
setattr()
delattr()
hasattr()
'''

