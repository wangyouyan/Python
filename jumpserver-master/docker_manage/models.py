# coding:utf-8
from django.db import models
from juser import models as user_models
# Create your models here.
import datetime

class docker_conf(models.Model):
    docker_host = models.CharField(max_length=48,verbose_name='主机名称')
    base_url = models.CharField(max_length=256,verbose_name='连接地址')




# user pull image record
class docker_image_pull_record(models.Model):
    operate_user = models.ForeignKey(user_models.User)
    operate_date = models.DateTimeField(default=datetime.datetime.now().date())
    image_name = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    progress = models.CharField(max_length=256,null=True,blank=True)


class pull_image_detail(models.Model):
    id = models.CharField(max_length=64,unique=True,primary_key=True)
    status = models.CharField(max_length=128)
    current = models.CharField(max_length=64,null=True,blank=True)
    total = models.CharField(max_length=64,null=True,blank=True)
    progress = models.CharField(max_length=256,null=True,blank=True)
    docker_image = models.ForeignKey(docker_image_pull_record)

