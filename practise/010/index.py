#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import event
import twisted

from event import event_drive

class MyClass(event_drive.BaseHandler):

    def execute(self):
        pass

#注册一个事件
event_drive.event_list.append(MyClass)
event_drive.run()