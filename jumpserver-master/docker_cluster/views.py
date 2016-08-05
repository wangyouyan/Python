# coding=utf-8
from django.shortcuts import render
from jumpserver.api import *
# Create your views here.


def docker_cluster(request):
    header_title, path1, path2 = u'Docker集群概况', u'Docker集群管理', u'Docker集群概况'
    return my_render('docker_cluster/docker_cluster_index.html',locals(),request)