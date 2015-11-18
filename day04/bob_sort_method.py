#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#Description:This program is mainly practicing the bob sort method(冒泡算法)
#实际上是一个排列组合

li = [13,22,18,33,99,15] 

for n in range(1,len(li)):
	for m in range(len(li)-n):
		#获取m个值
		num1 = li[m]
		#获取m+1个值
		num2 = li[m+1]
		if num1 > num2:
		#将较大的值放在右侧
			temp = li[m]
			li[m] = num2
			li[m+1] = temp
print li
'''
###算法解析####
#for m in range(5):
num1 = li[4]
num2 = li[5]
if num1 > num2:
	temp = li[4]
	li[4] = li[5]
	li[5] = temp
print li
###
num1 = li[3] 
num2 = li[4] 
if num1 > num2: 
        temp = li[3] 
        li[3] = li[4] 
        li[4] = temp
print li
###
num1 = li[2]
num2 = li[3]
if num1 > num2:
        temp = li[2]
        li[2] = li[3]
        li[3] = temp
print li
###
num1 = li[1]
num2 = li[2]
if num1 > num2:
        temp = li[1]
        li[1] = li[2]
        li[2] = temp
print li
'''
