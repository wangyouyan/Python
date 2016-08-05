#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

class AlexError(Exception):
    def __init__(self,msg=None):
        self.message = msg
    def __str__(self):
        if self.message:
            return self.message
        else:
            return 'Alex error'

try:
    raise AlexError('Alexalwaysmakemistakes')
except Exception,e:
    print e