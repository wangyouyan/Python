#!/usr/bin/env python
#coding:utf-8


import commands


def monitor():
    shell_command = 'uptime'

    status,result = commands.getstatusoutput(shell_command)
    value_dic = {}

    if status == 0: #cmd exec error
        
        uptime = result.split(',')[:1][0]
        
        # if linux
        # load1,load5,load15 = result.split('load average:')[1].split(',')

        # if mac 
        load1, load5, load15 = result.split('load averages:')[1].strip().split(' ');
        value_dic= {
            'uptime': uptime,
            'load1': load1,
            'load5': load5,
            'load15': load15,
        }

    return value_dic
