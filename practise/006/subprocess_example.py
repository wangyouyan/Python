#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import subprocess
import commands
'''
cmd = subprocess.call(["pwd"],shell=True)
cmd1 = subprocess.check_call(["hostname"],shell=True)
cmd2 = subprocess.check_output(["df"],shell=True)

print cmd
print('---------------')
print cmd1
print('***********')
print cmd2
'''
'''
a = commands.getoutput('pwd')
b = commands.getstatus('/Users/Rain/Python/day06//data_to_qq.txt')
c = commands.getstatusoutput('pwd')

cmd = subprocess.Popen(["ls -l"],shell=True)
#subprocess.Popen可以启动一个程序

print cmd

print('--------------')
print a
print('==============')
print b
print('**************')
print c


t = subprocess.Popen(["python"],stdin=subprocess.PIPE,stdout=subprocessIPE,stderr=subprocess.PIPE)
t.stdin.write("print 1\n")
t.stdin.write("print 1\n")
t.stdin.write("print 1\n")
t.communicate()
'''
#以下两种方法都可以
result = subprocess.check_output("df -h",shell=True)
result1 = subprocess.check_output(["df","-h"])
result2 = subprocess.check_output(["ls","-l","|","grep","test"],shell=True)
print result
print("----------")
print result1
print("**********")
print result2