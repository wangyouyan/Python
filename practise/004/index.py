#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import json,os

def fetch(backend):
	backend_title = 'backend %s' % backend
	record_list = []
	with open('haproxy.cfg') as obj:
		flag = False 
		for line in obj:
			line = line.strip()
			if line == backend_title:
				flag = True
				continue
			if flag and line.startswith('backend'):
				flag = False
				break

			if flag and line:
				record_list.append(line)

		return record_list

if __name__=='__main__':
	print "1. 获取相关配置; 2. 添加backend主机; 3. 删除backend主机"
	num = raw_input('请输入序号:') 
	data = raw_input('请输入内容->')
	if num == '1':
		fetch(data)
	else:
		dict_data = json.loads(data)
		if num == '2':
			#add(dict_data)	
			pass
		elif num == '3':
			#remove(dict_data)
			pass
		else:
			pass
