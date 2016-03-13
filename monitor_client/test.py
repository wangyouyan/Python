#!/usr/bin/env python
# -*- coding:utf-8 -*-

from plugins import plugin_api

# print plugin_api.get_load_info()
s = "get_load_info"
func = getattr(plugin_api, s)
print func()