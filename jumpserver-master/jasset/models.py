# coding: utf-8

import datetime
from django.db import models
from juser.models import User, UserGroup

ASSET_ENV = (
    (1, U'生产环境'),
    (2, U'STAG环境'),
    (3, u"总部Ceph"),
    (4, u"Virtual"),
    )

ASSET_STATUS = (
    (1, u"已使用"),
    (2, u"未使用"),
    (3, u"报废")
    )

ASSET_TYPE = (
    (1, u"物理机"),
    (2, u"虚拟机"),
    (3, u"交换机"),
    (4, u"路由器"),
    (5, u"防火墙"),
    (6, u"Docker"),
    (7, u"其他")
    )


class AssetGroup(models.Model):
    GROUP_TYPE = (
        ('P', 'PRIVATE'),
        ('A', 'ASSET'),
    )
    name = models.CharField(max_length=80, unique=True)
    comment = models.CharField(max_length=160, blank=True, null=True)

    def __unicode__(self):
        return self.name


class IDC(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'机房名称')
    bandwidth = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name=u'机房带宽')
    linkman = models.CharField(max_length=16, blank=True, null=True, default='', verbose_name=u'联系人')
    phone = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name=u'联系电话')
    address = models.CharField(max_length=128, blank=True, null=True, default='', verbose_name=u"机房地址")
    network = models.TextField(blank=True, null=True, default='', verbose_name=u"IP地址段")
    date_added = models.DateField(auto_now=True, null=True)
    operator = models.CharField(max_length=32, blank=True, default='', null=True, verbose_name=u"运营商")
    comment = models.CharField(max_length=128, blank=True, default='', null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"IDC机房"
        verbose_name_plural = verbose_name


class Asset(models.Model):
    """
    asset modle
    """
    ip = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"主机IP")
    other_ip = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"其他IP")
    hostname = models.CharField(unique=True, max_length=128, verbose_name=u"主机名")
    port = models.IntegerField(blank=True, null=True, verbose_name=u"端口号")
    group = models.ManyToManyField(AssetGroup, blank=True, verbose_name=u"所属主机组")
    username = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"管理用户名")
    password = models.CharField(max_length=256, blank=True, null=True, verbose_name=u"密码")
    use_default_auth = models.BooleanField(default=True, verbose_name=u"使用默认管理账号")
    idc = models.ForeignKey(IDC, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'机房')
    mac = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"MAC地址")
    # remote_ip = models.CharField(max_length=16, blank=True, null=True, verbose_name=u'远控卡IP')
    remote_ip = models.OneToOneField('Idrac',blank=True, null=True, verbose_name=u'远控卡IP')
    brand = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'硬件厂商型号')
    cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'CPU')
    memory = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'内存')
    disk = models.CharField(max_length=1024, blank=True, null=True, verbose_name=u'硬盘')
    system_type = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"系统类型")
    system_version = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"系统版本号")
    system_arch = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"系统平台")
    cabinet = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'机柜号')
    position = models.IntegerField(blank=True, null=True, verbose_name=u'机器位置')
    number = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'资产编号')
    status = models.IntegerField(choices=ASSET_STATUS, blank=True, null=True, default=1, verbose_name=u"机器状态")
    asset_type = models.IntegerField(choices=ASSET_TYPE, blank=True, null=True, verbose_name=u"主机类型")
    env = models.IntegerField(choices=ASSET_ENV, blank=True, null=True, verbose_name=u"运行环境")
    sn = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"SN编号")
    date_added = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=u"是否激活")
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.hostname


class AssetRecord(models.Model):
    asset = models.ForeignKey(Asset)
    username = models.CharField(max_length=30, null=True)
    alert_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)


class AssetAlias(models.Model):
    user = models.ForeignKey(User)
    asset = models.ForeignKey(Asset)
    alias = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.alias


# 租户信息 add by Rain
class Tenant_info(models.Model):
    env_type_value = (
        ("stag", u"staging环境"),
        ("prod", u"生产环境"),
    )
    env_type = models.CharField(u"环境类型", choices=env_type_value, max_length=32, default="stag")
    tenant_name = models.CharField(max_length=48,verbose_name=u'租户名称')
    user_name = models.CharField(max_length=48,verbose_name=u'用户名')
    user_passwd = models.CharField(max_length=48,verbose_name=u'密码')
    admin_host = models.CharField(max_length=1024,verbose_name=u'管理主机',null=True,blank=True)
    net_work = models.CharField(max_length=1024,verbose_name=u'管理网络',null=True,blank=True)
    comments = models.TextField(max_length=1024,verbose_name=u'备注信息',null=True,blank=True)

    class Meta:
        verbose_name = "租户信息"
        verbose_name_plural = "租户信息"

    def __unicode__(self):
        return self.tenant_name

# Idrac 信息
class Idrac(models.Model):
    Idrac_ip = models.GenericIPAddressField(verbose_name=u"IDRAC管理地址")
    Idrac_user = models.CharField(max_length=48, verbose_name=u"Idrac管理用户", null=True, blank=True)
    Idrac_passwd = models.CharField(max_length=48, verbose_name=u'IDrac管理密码', null=True, blank=True)

    class Meta:
        verbose_name = "Idrac"

    def __unicode__(self):
        return self.Idrac_ip

# 主机信息 add by Rain
# class Host_info(models.Model):
#     env_type_value = (
#         ("stag", u"staging环境"),
#         ("prod", u"生产环境"),
#         ("zongbu", u"总部Ceph"),
#         ("virtual", u"Virtual"),
#     )
#     env_type = models.CharField(u"环境类型", choices=env_type_value, max_length=32, default="stag",null=True,blank=True)
#     host_name = models.CharField(verbose_name=u"服务器名称", max_length=48)
#     SN = models.CharField(verbose_name=u"服务器SN号", max_length=126,null=True,blank=True)
#     host_ip = models.GenericIPAddressField(verbose_name=u"服务器IP地址")
#     host_models = models.CharField(max_length=48, verbose_name=u"服务器型号",null=True,blank=True)
#     host_port = models.CharField(max_length=48,verbose_name=u'SSH port',null=True,blank=True,default=22)
#     host_user = models.CharField(max_length=48,verbose_name=u"主机用户",null=True,blank=True)
#     host_passwd = models.CharField(max_length=48,verbose_name=u"主机密码",null=True,blank=True)
#     Idrac = models.OneToOneField(Idrac,null=True,blank=True)
#     comments = models.TextField(verbose_name=u"备注",null=True,blank=True)
#
#     class Meta:
#         verbose_name = "主机信息"
#         verbose_name_plural = "主机信息"
#
#     def __unicode__(self):
#         return self.host_name


# 管理地址
class Url_info(models.Model):
    url = models.URLField()
    env_type_value = (
        ("stag", u"staging环境"),
        ("prod", u"生产环境"),
        ("shijiazhuang", u"石家庄环境"),
        ("office", u"生产环境"),
    )
    env_type = models.CharField(u"环境类型", choices=env_type_value, max_length=32, default="staging")
    server_name = models.CharField(verbose_name=u"服务名称",max_length=48,null=True,blank=True)
    user_name = models.CharField(max_length=48,verbose_name=u"登录名",null=True,blank=True)
    user_passwd = models.CharField(max_length=48,verbose_name=u"密码",null=True,blank=True)
    host_type = models.CharField(max_length=48,verbose_name=u"主机类型",null=True,blank=True)
    comments = models.TextField(verbose_name=u"备注",null=True,blank=True)

    class Meta:
        verbose_name = "管理地址"
        verbose_name_plural = "管理地址"

    def __unicode__(self):
        return self.url



# 虚拟化平台
class Virtual_platform(models.Model):
    virtual_type_value = (
        ("Xenserver", "Xenserver"),
        ("Vmware", "Vmware"),
    )
    platform_name = models.CharField(u'平台名称', max_length=48)
    virtual_type = models.CharField(u"虚拟化类型", choices=virtual_type_value, max_length=48,null=True,blank=True)
    zone = models.CharField(verbose_name=u"区域", max_length=48,null=True,blank=True)
    # host_info = models.OneToOneField(Host_info,verbose_name=u'主机信息',null=True,blank=True)
    host_info = models.OneToOneField(Asset, verbose_name=u'主机信息', null=True, blank=True)
    class Meta:
        verbose_name = "虚拟主机平台"
        verbose_name_plural = "虚拟主机平台"

    def __unicode__(self):
        return self.platform_name


# 虚拟化主机
class Virtual_host(models.Model):
    host_ip = models.GenericIPAddressField(verbose_name=u"虚拟主机IP")
    host_name = models.CharField(max_length=48, verbose_name=u"虚拟主机名称")
    # host_user = models.CharField(max_length=48,verbose_name=u'用户名',null=True,blank=True)
    # host_passwd = models.CharField(max_length=48, verbose_name=u'密码',null=True,blank=True)
    host_comments = models.CharField(max_length=128,verbose_name=u"备注",blank=True,null=True)
    server = models.ForeignKey("Virtual_platform")

    class Meta:
        verbose_name = "虚拟主机"
        verbose_name_plural = "虚拟主机"

    def __unicode__(self):
        return self.host_ip