# coding:utf-8
from django.conf.urls import patterns, include, url
from docker_manage.views import  *
from docker_manage import django_websocket
urlpatterns = patterns('',
    url(r'^index/$',docker_index,name='docker_index'),
    url(r'^list/$', docker_list, name='docker_list'),
    url(r'^image/list/$',docker_image_list,name="docker_image_list"),
    url(r'^docker/create/$',create_docker,name="create_docker"),

    url(r'^operate/docker/$',operate_docker,name="operate_docker"),
    url(r'^ws', django_websocket.index, name="websocket"),

    url(r'^image/add',search_image,name="image_search"),
    url(r'^image/pull',pull_image,name="pull_image"),
    url(r'^pull_image_progress',pull_image_progress,name="pull_image_progress"),
    url(r'^remove/image',remove_image,name="remove_image"),
    url(r'^image_history/',get_pull_image_progress,name="image_history"),

    url(r'^docker/volume/list/',volume_list,name="docker_volume_list"),
    url(r'^docker/volume/create/',volume_create,name="docker_volume_create"),
    url(r'^docker/volume/delete/',removre_volume,name="docker_volume_remove"),


   url(r'^docker/edit/',docker_edit,name="docker_edit"),
   url(r'^docker/host/',docker_host,name="docker_host"),
   url(r'^host/add',docker_host_add,name="docker_host_add"),
   url(r'^connect/test',docker_connect_test,name="docker_connect_test"),
   url(r'^docker_host/del',docker_host_del,name="docker_host_del"),
   url(r'^docker_host/edit',docker_host_edit,name="docker_host_edit"),

)