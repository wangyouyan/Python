#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from django import forms
class ImportForm(forms.Form):
    HOST_TYPE_LIST = (
        (1,'物理机'),
        (2,'虚拟机')
    )
    host_type = forms.IntegerField(
        widget=forms.Select(choices=HOST_TYPE_LIST)
    )
    hostname = forms.CharField()

    import json
    fr = open('db_admin')
    data = fr.read()
    data_tuple = json.loads(data)

    admin = forms.IntegerField(
        widget=forms.Select(choices=data_tuple)
    )

    def __init__(self,*args,**kwargs):
        super(ImportForm,self).__init__(*args,**kwargs)
        import json
        fr = open('db_admin')
        data = fr.read()
        data_tuple = json.loads(data)
        self.fields['admin'].widget.choices = data_tuple

