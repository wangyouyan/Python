#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()

@register.simple_tag
def my_simple_time(v1,v2,v3):
    return  v1 + v2 + v3

@register.simple_tag
def my_input(id,arg):
    result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
    return mark_safe(result)