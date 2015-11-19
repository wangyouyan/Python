#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import pexpect,sys


child = pexpect.spawn('ssh root@192.168.1.21') #spawn启动scp程序
fout = file('mylog.txt','w')
child.logfile = fout

child.expect('Password:')   #expect方法等待子进程产生的输出，判断是否匹配定义的字符串'Password:'
child.sendline(mypassword)  #匹配后则发送密码串进行回应
child.expect('#')
child.expect('ls /home')
child.expect('#')




