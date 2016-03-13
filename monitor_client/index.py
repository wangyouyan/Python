#!/usr/bin/env python
#coding:utf-8

#客户端根据模版发布信息
import json
import time
from plugins import plugin_api
from backend.sqlhelper import *
import threading

hostname = 'No.1'

def get_config(rediscli,templatename):
    data = rediscli.get(templatename)
    config = json.loads(data)
    
    return config

def get_info(rediscli,data,value):
    # value = {"interval": 6, "last_time": 0, "plugin_name": "get_load_info"},
    func = getattr(plugin_api,value['plugin_name'])
    #data['data'] = func()
    print func()
    #print data['type']
    #rediscli.publish(json.dumps(data))



def monitor_info(rediscli,data,value):
    func = getattr(plugin_api,value['plugin_name'])
    client_info = func()
    # {'load1': '2.28', 'load15': '1.78', 'uptime': ' 7:04  up 2 days', 'load5': '2.06'}
    for k, v in value['threshold']:
        cli_val = client_info.get(k, None)
        if not cli_val:
            pass
        else:
            import operator
            for threshold_ele in v:
                """
                op = getattr(operator, threshold_ele['operator'])
                ret = op(cli_val, v['val'])
                if ret:
                    print 'alert'
                """
                """
                if threshold_ele['operator']:
                    cli_val = getattr(operator, threshold_ele['formula'])(cli_val)
                op = getattr(operator, threshold_ele['operator'])
                ret = op(cli_val, v['val'])
                if ret:
                    print 'alert'
                """
                if threshold_ele['operator']:
                    cli_val = getattr(operator, threshold_ele['formula'])(cli_val)
                op = getattr(operator, threshold_ele['operator'])
                ret = op(cli_val, v['val'])
                if ret:
                    if not threshold_ele.get('complex', None):
                        print 'alert'
                    else:
                        currenttime,interval,reltime = time.time(), v['complex']['interval'],v['complex']['relative_time']
                        if currenttime < reltime + interval:
                            v['complex']['has_times'] += 1
                        else:
                            v['complex']['has_times'] = 0
                            v['complex']['relative_time'] = currenttime

                        if v['complex']['has_times'] >= v['complex']['times']:
                            print 'alert'
                            v['complex']['has_times'] = 0
                            v['complex']['relative_time'] = currenttime






"""
{
    "load": {"interval": 6, "last_time": 0, "plugin_name": "get_load_info"},
    "cpu": {"interval": 5, "last_time": 0, "plugin_name": "get_cpu_info"}, 
    "memory": {"interval": 3, "last_time": 0, "plugin_name": "get_memory_info"}
}
"""
"""
template = {
    "load": {
        "last_time":0,
        "interval": 10,
        "plugin_name": "get_load_info",
        "threshold": {
            "load1": [
                {"operator": "gt", "formula": None, "val": "1.1"},
                {"operator": "lt", "formula": None, "val": "5"}
            ],
            "load5": [
                {"operator": "gt", "formula": None, "val": "1.0", "complex":{"interval": 30, "times": 5, "has_times": 0, "relative_time": 0}},
                {"operator": "lt", "formula": None, "val": "5"}
            ]
        }
    },
}
"""

def run(rediscli,config):
    """
    config = {
        time.time()
        last_time-->11:10:50
        "load": {"interval": 6, "last_time": 0, "plugin_name": "get_load_info"},
        "cpu": {"interval": 5, "last_time": 0, "plugin_name": "get_cpu_info"},
        "memory": {"interval": 3, "last_time": 0, "plugin_name": "get_memory_info"}
    }
    """
    while True:
        for key,value in config.items():
            # key = "load","cpu"
            # value = {"interval": 6, "last_time": 0, "plugin_name": "get_load_info"},

            data = {'hostname':hostname}

            currenttime,interval,pretime = time.time(),value['interval'],value['last_time']
            # currenttime 1453601463.166203
            # interval = 6
            # pretime = 1453601373.064652
            if currenttime - pretime < interval:
                print 'waiting...'
            else:
                # data['type'] = key
                t = threading.Thread(target=get_info,args=(rediscli,data,value))
                t.start()
                value['last_time'] = currenttime
                
        time.sleep(1)
        
        
if __name__ == '__main__':
    # template = 'template_1'
    #redis_cli = RedisHelper()
    #config = get_config(redis_cli, template)
    config = {
        "load": {"interval": 6, "last_time": 0, "plugin_name": "get_load_info"},
        #"cpu": {"interval": 5, "last_time": 0, "plugin_name": "get_cpu_info"},
        #"memory": {"interval": 3, "last_time": 0, "plugin_name": "get_memory_info"}
    }
    redis_cli = object()
    run(redis_cli,config)





