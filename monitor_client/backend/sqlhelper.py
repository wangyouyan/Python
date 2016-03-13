#!/usr/bin/env python
#coding:utf-8

import redis

class RedisHelper:
    
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1',port=6379)
        self.__channel = 'sb107_8'
        
        
    def get(self,key):
        return self.__conn.get(key)
    
    def set(self,key,value):
        return self.__conn.set(key, value)
    
    def set_ex(self,key,value,expire):
        return self.__conn.set(name=key, value=value,ex=expire)
    
    def delete(self,key):
        self.__conn.delete(key)
        
    def publish(self,msg):
        self.__conn.publish(self.__channel, msg)
        
    def subscribe(self):
        '''
        @return: 通过阻塞的方式获取订阅的数据 pubsub.parse_response() 
        '''
        pubsub = self.__conn.pubsub()
        pubsub.subscribe(self.__channel)
        pubsub.parse_response()
        return pubsub
    