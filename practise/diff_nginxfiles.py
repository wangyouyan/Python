#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import difflib,sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]

except Exception,e:
    print "Error:"+str(e)
    print "Usage: diff_nginxfiles filename1 filename2"
    sys.exit()

def readline(filename):
    try:
        fileHandle = open(filename,'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:'+str(error))
        sys.exit()

if textfile1=="" or textfile2=="":
    print "Usage: diff_nginxfiles filename1 filename2"
    sys.exit()

text1_lines = readline(textfile1)
text2_lines = readline(textfile2)

d = difflib.HtmlDiff() #创建HtmlDiff()类对象
print d.make_file(text1_lines,text2_lines) #通过make_file方法输出HTML格式的比对结果