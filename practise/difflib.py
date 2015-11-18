#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import difflib

#定义字符串1
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""
#以行进行分割，以便进行对比
text1_lines = text1.splitlines()
#定义字符串2
text2 = """text2:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5
add string
"""
text2_lines = text2.splitlines()
#创建Differ()函数
d = difflib.Differ()
#采用compare方法对字符串进行比较
#diff = d.compare(text1_lines,text2_lines)
#print '\n'.join(list(diff))


d = difflib.HtmlDiff()
print '\n'.join(list(diff))

