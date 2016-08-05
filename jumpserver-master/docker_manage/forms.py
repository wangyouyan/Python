# coding:utf-8
from django import forms
from  api import  *
from models import  docker_conf
def get_choice():
    host_choice = ()
    mydocker = Docker_manage()
    for host in mydocker.all_docker_images.keys():
        temp_choice = (host, host)
        host_choice += (temp_choice,)
    images_choice = ()
    try:
        host, image_list = mydocker.all_docker_images.items()[0]
        for image in image_list:
            temp_choice = (image["RepoTags"][0], image["RepoTags"][0])
            images_choice += (temp_choice,)
    except Exception as e:
        print e
        host_choice = ""
        images_choice = ""
    # print images_choice
    return  host_choice,images_choice

def get_volume(docker_host):
    mydocker = Docker_manage()
    volume_choice = ()
    all_volumes = mydocker.volume_list(docker_host)
    for host,volumes  in all_volumes.items():
        print host,volumes
        for volume in volumes["Volumes"]:
            temp_choice  = ("%s_%s"%(host,volume["Mountpoint"]),volume["Name"])
            volume_choice +=(temp_choice,)
    return volume_choice


# mount type
def get_mount_type():
    mount_type_choice = (
        ('auto',u'自动创建数据卷'),
        ('nomount',u'不挂载数据卷'),
        ('input',u'手动指定'),
    )
    return  mount_type_choice

def get_port():
    port_choice = (
        ("default",u'默认'),
        ("port",u"端口"),
        # ("portrange",u"端口范围"),
    )
    return port_choice


class create_container(forms.Form):
    def __init__(self, *args, **kwargs):
        # dynamic loading ....
        super(create_container, self).__init__(*args, **kwargs)
        self.fields["docker_host"].choices = get_choice()[0]
        self.fields["container_images"].choices = get_choice()[1]
        # self.fields["volume_name"].choices = get_volume("all")
        self.fields["mount_type"].choices = get_mount_type()
        self.fields["port_type"].choices = get_port()

    container_name = forms.CharField(label=u'容器名称',max_length=48)
    host_name = forms.CharField(label=u'主机名称',max_length=48)
    docker_host = forms.ChoiceField(label=u'容器主机',widget=forms.widgets.Select(choices=(),attrs={
        'class':"form-control",
        "onchange":"change_host(this)",
    }))
    container_images = forms.ChoiceField(label=u'容器镜像',widget=forms.widgets.Select(choices=(),attrs={
        'class':"form-control",
    }))

    port_type  = forms.ChoiceField(label=u'容器端口',widget=forms.widgets.Select(
        attrs={
            'class': "form-control",
            "onclick": "change_port_type(this)",
        }
    ))
    port = forms.CharField(label=u"端口",widget=forms.widgets.Input(
        attrs={
            'placeholder': "8000:8080;7096:8096  请按照此格式添加 容器端口:宿主机端口;容器端口:宿主机端口",
        }

    ))
    mount_type = forms.ChoiceField(label=u'数据卷挂载',widget=forms.widgets.Select(
        attrs={
            'class': "form-control",
            "onclick": "change_mount_type(this)",
        }
    ))

    volume_name  = forms.ChoiceField(label=u'数据卷',widget=forms.widgets.Select(
        attrs={
            'class': "form-control",
        }
    ))
    docker_mount = forms.CharField(max_length=128,label=u'数据卷挂载位置')

    command = forms.CharField(label=u'命令',max_length=128)

    # host_choice, images_choice = get_choice()



class pull_image_form(forms.Form):
    host_choice, images_choice = get_choice()
    registry = forms.CharField(label=u'registry',max_length=128,widget=forms.widgets.Input(attrs={
        'placeholder':"docker.io",
        'value':"docker.io",
        }))
    search_name = forms.CharField(label=u'search',max_length=128)
    docker_host = forms.CharField(label=u'容器主机',max_length=48,widget=forms.widgets.Select(choices=host_choice,attrs={
        'class':"form-control",
    }))




class create_volume(forms.Form):
    def __init__(self, *args, **kwargs):
        # dynamic loading ....
        super(create_volume, self).__init__(*args, **kwargs)
        self.fields["docker_host"].choices = get_choice()[0]
    docker_host = forms.ChoiceField(label=u'容器主机',widget=forms.widgets.Select(choices=(),attrs={
        'class':"form-control",
    }))
    volume_name = forms.CharField(label=u'Volume name',max_length=48)


class docker_edit_form(forms.Form):
    docker_name = forms.CharField(label=u'容器新名称',max_length=128)


class docker_conf_form(forms.ModelForm):
    class Meta:
        model = docker_conf
        fields = "__all__"