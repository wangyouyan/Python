#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

# event_drive.py

event_list = []


def run():
    for event in event_list:
        obj = event()
        obj.execute()


class BaseHandler(object):
    """
    用户必须继承该类，从而规范所有类的方法（类似于接口的功能）
    """
    def execute(self):
        raise Exception('you must overwrite execute')