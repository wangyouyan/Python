# coding:utf-8
from django.conf.urls import patterns, include, url
from jasset.views import *

urlpatterns = patterns('',
    url(r'^asset/add/$', asset_add, name='asset_add'),
    url(r"^asset/add_batch/$", asset_add_batch, name='asset_add_batch'),
    url(r'^asset/list/$', asset_list, name='asset_list'),
    url(r'^asset/del/$', asset_del, name='asset_del'),
    url(r"^asset/detail/$", asset_detail, name='asset_detail'),
    url(r'^asset/edit/$', asset_edit, name='asset_edit'),
    url(r'^asset/edit_batch/$', asset_edit_batch, name='asset_edit_batch'),
    url(r'^asset/update/$', asset_update, name='asset_update'),
    url(r'^asset/update_batch/$', asset_update_batch, name='asset_update_batch'),
    url(r'^asset/upload/$', asset_upload, name='asset_upload'),
    url(r'^group/del/$', group_del, name='asset_group_del'),
    url(r'^group/add/$', group_add, name='asset_group_add'),
    url(r'^group/list/$', group_list, name='asset_group_list'),
    url(r'^group/edit/$', group_edit, name='asset_group_edit'),
    url(r'^idc/add/$', idc_add, name='idc_add'),
    url(r'^idc/list/$', idc_list, name='idc_list'),
    url(r'^idc/edit/$', idc_edit, name='idc_edit'),
    url(r'^idc/del/$', idc_del, name='idc_del'),


    # tenant info ..
    url(r'^tenant/list/$',tenant_list,name="tenant_list"),
    url(r'^tenant/add/$',tenant_add,name="tenant_add"),
    url(r'^tenant/del/$',tenant_del,name="tenant_del"),
    url(r'^tenant/edit/$',tenant_edit,name="tenant_edit"),
    url(r'^batch_add_tenant/$',tenant_batch_add,name="batch_add_tenant"),
    url(r'^tpl_add_tenant/$', tenant_tpl_add, name="batch_tpl_tenant"),


    # # manage host
    # url(r'^host/list/$',host_list,name="host_list"),
    # url(r'^host/add/$',host_add,name="host_add"),
    # url(r'^host/del/$',host_del,name="host_del"),
    # url(r'^host/edit/$',host_edit,name="host_edit"),
    # url(r'^host/detail',host_detail,name="host_detail"),
    # url(r'^batch_add_host/$', host_batch_add, name="batch_add_host"),
    # url(r'^tpl_add_host/$', host_tpl_add, name="batch_tpl_host"),

    # manage url
    url(r'^url/list/$',url_list,name="url_list"),
    url(r'^url/add/$',url_add,name="url_add"),
    url(r'^url/del/$',url_del,name="url_del"),
    url(r'^url/edit/$',url_edit,name="url_edit"),
    url(r'^batch_tpl_url/$', url_tpl_add, name="batch_tpl_url"),

    #  virtual platform
    url(r'^virtual_platform/list/$',virtual_platform_list,name="virtual_platform_list"),
    url(r'^virtual_platform/detail/$',virtual_platform_detail,name="virtual_platform_detail"),
    url(r'^virtual_platform/add/$',virtual_platform_add,name="virtual_platform_add"),
    url(r'^virtual_platform/del/$',virtual_platform_del,name="virtual_platform_del"),
    url(r'^virtual_platform/edit/$', virtual_platform_edit, name="virtual_platform_edit"),

    url(r'^virtual_host/del/$',virtual_host_del,name="virtual_host_del"),
    url(r'^virtual_host/edit/$',virtual_host_edit,name="virtual_host_edit"),
    url(r'^batch_add/virtual_host/$',batch_add_virtual_host,name="batch_add_virtual_host"),




)