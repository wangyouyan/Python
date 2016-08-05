#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

class SqlHelper:

    __static_instance = None

    def __init__(self):
        self.hostname = '0.0.0.0'
        self.port = 3306
        self.password = 'che001'
        self.username = 'otomat'


    @classmethod
    def instance(cls):
        #cls = SqlHelper
        if cls.__static_instance:
            return cls.__static_instance
        else:
            cls.__static_instance = SqlHelper()
            return cls.__static_instance

    def fetch(self):
        pass

    def remove(self):
        pass



