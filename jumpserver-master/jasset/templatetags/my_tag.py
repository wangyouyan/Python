#!/usr/bin/env python
# coding=utf-8
# created by Rain
from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError
import json
register = template.Library()
import time

@register.simple_tag
def tran_search_value(value,search_value):
    if search_value == "":
        return  value
    if search_value in value:
        return value.replace(search_value,"<span style='color:red' >%s</span>"%search_value)
    else:
        return  value

@register.filter
def tran_date(date_value):
    x = time.localtime(date_value)
    return time.strftime('%Y-%m-%d %H:%M:%S', x)

@register.filter
def tran_size(size_value):
    # if size_value/1024/1024 >1024:
    #    return  str(size_value/(1024**3))+"G"
    # elif size_value/1024/1024 <1024:
    #     return str(size_value/(1024**2))+"M"
    if size_value/1000/1000 >1000:
       return  str(size_value/(1000**3))+"G"
    elif size_value/1000/1000 <1000:
        return str(size_value/(1000**2))+"M"


@register.simple_tag
def tran_port(value,search_value):
    if value == []:
        return ""
    new_ret = ''
    for index,item in enumerate(value):

        if index>1:
            egg="..."
            return  new_ret+egg
        else:
            egg=""
        new_ret += item["IP"]+":"+str(item["PublicPort"])+"->"+str(item["PrivatePort"])+"/"+item["Type"]+"</br>"
    #  0.0.0.0:32770->9900/tcp
    return new_ret

@register.simple_tag
def tran_status(list1,counter):

    return list1[int(counter)-1]\

@register.simple_tag
def get_status_color(list1,counter):
    if list1[int(counter)-1]=="Error":
        return "#EE8262"
    else:
        return ""