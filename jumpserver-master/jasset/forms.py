# coding:utf-8
from django import forms

from jasset.models import IDC, Asset, AssetGroup,Tenant_info,Idrac,Url_info,Virtual_platform,Virtual_host


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset

        fields = [
            "ip", "other_ip", "hostname", "port", "group", "username", "password", "use_default_auth",
            "idc", "mac", "brand", "cpu", "memory", "disk", "system_type", "system_version",
            "cabinet", "position", "number", "status", "asset_type", "env", "sn", "is_active", "comment",
            "system_arch"
        ]


class AssetGroupForm(forms.ModelForm):
    class Meta:
        model = AssetGroup
        fields = [
            "name", "comment"
        ]


class IdcForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = ['name', "bandwidth", "operator", 'linkman', 'phone', 'address', 'network', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'network': forms.Textarea(
                attrs={'placeholder': '192.168.1.0/24\n192.168.2.0/24'})
        }


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant_info
        fields = ["env_type","tenant_name","user_name","user_passwd","admin_host","net_work","comments"]

class HostForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = "__all__"
        # exclude = ["Idrac"]

class IdracForm(forms.ModelForm):
    class Meta:
        model = Idrac
        fields = "__all__"

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url_info
        fields = "__all__"


class VirtualForm(forms.ModelForm):
    class Meta:
        model = Virtual_platform
        fields = '__all__'
        exclude = ["Host_info",]

class VirtualHostForm(forms.ModelForm):
    class Meta:
        model = Virtual_host
        fields = '__all__'
        exclude = ["server"]