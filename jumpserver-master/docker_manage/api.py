#!/usr/bin/env python
# coding=utf-8
# created by Rain
from django.db.models import Q
from docker import Client
import  ConfigParser
import json
import models
from dwebsocket import  *
class Docker_manage(object):
    #  初始化,读取配置文件，获取url，连接主机，获取主机容器
    def __init__(self,host_list=None):
        if __name__ == "__main__":
            self.conf = ConfigParser.ConfigParser()
            self.conf.read("../docker.conf")
            print self.conf.sections()
            self.docker_host_list = self.conf.sections()
            self.docker_base_url = {}
            for docker_host in self.docker_host_list:
                self.docker_base_url[docker_host]=self.conf.get(docker_host,"base_url")
        else:
            import models


            self.docker_host_list = models.docker_conf.objects.all()

            self.docker_base_url = {}
            for docker_host in self.docker_host_list:
                try:
                    cli = Client(docker_host.base_url)
                    cli.images()
                except:
                    # print docker_host.base_url,"is not valied.."
                    continue
                self.docker_base_url[docker_host.docker_host]=docker_host.base_url

        #  all docker
        self.all_docker_dic = {}

        # active docker
        self.docker_dic={}

        # pause docker
        self.pauser_docker_dic = {}

        # restart docker
        self.restart_docker_dic = {}

        # stop docker
        self.stop_docker_dic = {}

        self.docker_images = {}

        self.docker_images_pull = {}
        for docker_host,base_url in self.docker_base_url.items():
            cli = Client(base_url)
            self.docker_images[docker_host]= cli.images(all=True)
            self.docker_dic[docker_host]=cli.containers()
            self.all_docker_dic[docker_host] = cli.containers(all=True)
            self.pauser_docker_dic[docker_host]= cli.containers(filters={"status":"paused"})
            self.restart_docker_dic[docker_host] = cli.containers(filters={"status":"restarting"})
            self.stop_docker_dic[docker_host] = cli.containers(filters={"status":"exited"})


    # get active docker
    @property
    def get_active_docker(self):
        # print self.docker_dic
        docker_count = 0
        for k,v in self.docker_dic.items():
            docker_count = docker_count + v.__len__()
        return docker_count

    @property
    def get_paused_docker(self):
        docker_count = 0
        for k,v in self.pauser_docker_dic.items():
            docker_count = docker_count + v.__len__()
        return docker_count

    @property
    def get_restarting_docker(self):
        docker_count = 0
        for k,v in self.restart_docker_dic.items():
            docker_count = docker_count + v.__len__()
        return docker_count

    @property
    def get_stop_docker(self):
        docker_count = 0
        for k,v in self.stop_docker_dic.items():
            docker_count = docker_count + v.__len__()
        return docker_count

    # 获取all docker主机个数
    @property
    def host_count(self):
        return self.all_docker_dic.__len__()

    # 获取所有主机docker容器个数
    @property
    def all_docker_count(self):
        # print self.docker_dic
        docker_count = 0
        for k,v in self.all_docker_dic.items():
            docker_count = docker_count + v.__len__()
        return docker_count

    def docker_count(self,docker_host):
        return  self.all_docker_dic[docker_host].__len__()

    # 获取所有host名称
    @property
    def all_docker_host(self):
        return self.all_docker_dic
    # 根据host名称，获取对应容器
    def get_dockers(self,docker_host):

        return self.all_docker_dic[docker_host]

    def get_docker(self,docker_id):
        '''return a obj '''
        pass

    #  get images count
    @property
    def docker_image_count(self):
        docker_image_count = 0
        for k,v in self.docker_images.items():
            docker_image_count = docker_image_count + v.__len__()
        return docker_image_count

    # get all docker images
    @property
    def all_docker_images(self):
        return self.docker_images

    # get host  docker image
    def get_docker_images(self,docker_host):
        return self.docker_images[docker_host]

    # create docker such as  docker run
    def create_docker(self,docker_host,*create_kwargs):
        url = self.docker_base_url[docker_host]
        cli = Client(base_url=url)
        container_name,image,command,host_name,volume_name,docker_mount,volumes,ports = create_kwargs
        if not  ports:
            port_bindings = None
            docker_ports_list=None
        else:
            docker_ports_list = []
            print ports
            port_bindings = {}
            ports_list = ports.split(";")
            if len(ports_list)>1:
                for port_item in ports.split(";"):
                    print port_item
                    docker_port,host_port = port_item.split(":")
                    print docker_port,host_port
                    port_bindings[docker_port]=host_port
                    docker_ports_list.append(docker_port)
            else:
                docker_port,host_port = ports_list[0].split(":")
                port_bindings={
                    docker_port: host_port
                }
                docker_ports_list.append(docker_port)
            print port_bindings
        if volume_name and  docker_mount:
            binds=[
                "%s:%s"%(volume_name,docker_mount)
            ]
        else:
            binds= None
        container = cli.create_container(name=container_name,
                                         image=image,command=command,
                                         tty=True,stdin_open=True,
                                         hostname=host_name,
                                         volumes = volumes,
                                         ports=docker_ports_list,
                                         host_config = cli.create_host_config(binds=binds,port_bindings=port_bindings),

                                         )
        ret = cli.start(container.get("Id"))
        return ret


    def rename_docker(self,docker_host,docker_name,docker_new_name):
        # print "rename docker....",docker_new_name,docker_host,docker_name
        docker_name = docker_name.split("/")[1]
        url = self.docker_base_url[docker_host]
        cli = Client(base_url=url)
        cli.rename(docker_name,docker_new_name)
        return True

    def docker_operate(self,func,docker_host,container):
        url = self.docker_base_url[docker_host]
        cli = Client(base_url=url)
        print func,container
        try:
            if hasattr(cli,func):
                func1 = getattr(cli,func)
                func1(container)
            else:
                raise Exception
                return False
        except Exception as e :
            print e
            return e
        return True

    # kill a container
    def stop_docker(self,docker_host,container):
        return self.docker_operate("stop",docker_host,container)


    # start a container
    def start_docker(self,docker_host,container):
        return self.docker_operate("start", docker_host, container)


    def remove_docker(self,docker_host,container):
        return self.docker_operate("remove_container", docker_host, container)


    def  pause_docker(self,docker_host,container):
        return self.docker_operate("pause", docker_host, container)



    def unpause_docker(self,docker_host,container):
        return self.docker_operate("unpause", docker_host, container)


    def restart_docker(self,docker_host,container):
        return self.docker_operate("restart", docker_host, container)


    def search_images(self,image_name,docker_host):
        url = self.docker_base_url[docker_host]
        cli = Client(base_url=url)
        image_list = []
        for i in cli.search(image_name):
            image_list.append(i)
        return image_list

    def pull_image_from_name(self,image_name,docker_host):
        url = self.docker_base_url[docker_host]
        cli = Client(base_url=url)
        self.docker_images_pull[image_name] = cli.pull(image_name, stream=True)
        print self.docker_images_pull
        return None

    def remove_image_in_docker_host(self,image_name,docker_host):
        url = self.docker_base_url[docker_host]
        cli = Client(base_url=url)
        print "remove %s" %image_name
        cli.remove_image(image=image_name)
        return True



    # volume list
    def volume_list(self,docker_host):
        if docker_host == "all":
            all_volumes = {}
            for docker_host,url  in self.docker_base_url.items():
                cli = Client(base_url=url)
                all_volumes[docker_host]=cli.volumes()
        else:
            url = self.docker_base_url[docker_host]
            cli = Client(base_url=url)
            all_volumes={docker_host:cli.volumes()}
        return all_volumes


    # create volume
    def create_volume(self,docker_host,voulme_name=None):
        url = self.docker_base_url[docker_host]
        cli = Client(base_url=url)
        if voulme_name:
            cli.create_volume(voulme_name)
        else:
            cli.create_volume()
        return  True
    # remove volume
    def remove_volume(self,docker_host,volume_name):
        print docker_host ,volume_name
        url = self.docker_base_url[docker_host]
        cli = Client(base_url=url)
        cli.remove_volume(volume_name)
        return True

    # @accept_websocket
    def pull_image_progress(self,request):
        message = request.websocket.wait()
        image_name,docker_host = message.split("|")
        # print image_name,docker_host
        # print self.docker_images_pull
        for line in self.docker_images_pull[image_name]:
            a = json.loads(line)
            try:
                if "Trying to pull repository" in  a["status"]:
                    docker_image_pull_record = models.docker_image_pull_record()
                    docker_image_pull_record.operate_user = request.user
                    docker_image_pull_record.image_name =  image_name
                    docker_image_pull_record.status = "Start pull.."
                    docker_image_pull_record.save()
                else:

                    obj = models.pull_image_detail.objects.filter(id=a["id"])
                    if(obj):
                        obj = models.pull_image_detail.objects.get(id=a["id"])
                        obj.status=a["status"]
                        if  a.has_key("progress"):
                            obj.progress = a["progress"]
                            obj.current = a["progressDetail"]["current"]
                            obj.total = a["progressDetail"]["total"]
                            obj.save()
                    else:
                        obj = models.pull_image_detail()
                        obj.status = a["status"]
                        obj.id=a["id"]
                        docker_image_pull_record = models.docker_image_pull_record.objects.get(operate_user=request.user,image_name=image_name)
                        obj.docker_image = docker_image_pull_record

                        obj.save()
            except Exception as e :
                print e
            request.websocket.send(line)





if __name__ == "__main__":
    mydocker = Docker_manage()
    # mydocker.create_docker("docker01",)
