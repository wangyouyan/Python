#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    #id 默认会创建一个id的列
    name = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now=True)
    uptime = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=32,null=True)
    email2 = models.EmailField(max_length=32,default='123@aliyun.com')
    ip = models.GenericIPAddressField(protocol="ipv4",null=True,blank=True)
    #img = models.ImageField(null=True,blank=True,upload_to="upload")
    file = models.FilePathField(null=True,blank=True,path='upload')

    def __unicode__(self):
        return self.name


