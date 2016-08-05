# from django.test import TestCase
import json
# Create your tests here.

# host_choice = ()
# for host in a.keys():
#     tmp_choice = (host,host)
#     host_choice+=(tmp_choice,)
#
# print host_choice
#
# images_choice = ()
# host, image_list = a.items()[0]
# for image in image_list:
#     temp_choice = (image["Id"], image["RepoTags"])
#     images_choice += (temp_choice,)
# print images_choice
from  docker import *
url = "tcp://172.16.13.38:2375"
cli = Client(base_url=url)
# all = cli.containers(all=True)
# print all
# for i in all:
#     print i
    # print i["Names"]
    # print i["Id"]
# print  cli.images()
# image = cli.get_image('docker.io/centos:latest')
# image_tar = open("/tmp/centos.tar","w")
# image_tar.write(image.data)
# image_tar.close()
# print cli.volumes()

# cli.create_container("centos",command="/bin/bash",hostname="docker02",name="docker02",
#                      volumes=["/data"],host_config=cli.create_host_config(binds=["/data:/tmp/data"])
#                      )
# cli.start("docker02")
#
# container_id = cli.create_container('centos', 'ls', volumes=['/mnt/vol1', '/mnt/vol2'])
# cli.start(container_id, binds={
#     '/home/user1/':
#         {
#             'bind': '/mnt/vol2',
#             'ro': False
#         },
#     '/var/www':
#         {
#             'bind': '/mnt/vol1',
#             'ro': True
#         }
# }
cli.create_volume(name="test_volume")
cli.rename("bvgfhndgh","testtest")
#
# container_id = cli.create_container(
#     'centos', '/bin/bash', name="ffas",tty=True,stdin_open=True,
#     volumes=None,ports=[12434,3434],
#     host_config=cli.create_host_config(
#         port_bindings = {
#             12434:8180,
#             3434:8899,
#
#         }
#     )
# )
# print(container_id)


# cli.start(container="docker01")
# a = cli.volumes()
# print type(a)
# print json.dumps(a,indent=4)
# cli.create_volume("test")
# cli.remove_image("docker.io/ipython/notebook:latest")
# for i in   cli.search("centos"):
#
#     image_name = i["name"]
#     print image_name,
#     for line in cli.pull(image_name,stream=True):
#         a = json.loads(line)
#
#         if a.has_key("progressDetail") :
#             if a["progressDetail"]!={}:
#                 print a["progressDetail"]["total"]
#                 break
# # print cli.pull("centos")

    # print json.dumps(json.loads(line),indent=4)
#     cli.start(i["Id"])
# print cli.containers(filters={"status":"paused"})
# print dir(cli.stats("4b806bcbbd3d487d0818bcbe32ce521f60a1608ce06881dd226c9973118d0819"))
# stats_obj =  cli.stats("4b806bcbbd3d487d0818bcbe32ce521f60a1608ce06881dd226c9973118d0819")
# for i in stats_obj:
#     a = json.loads(i)
#     print a["precpu_stats"]

# cli.start("4b806bcbbd3d487d0818bcbe32ce521f60a1608ce06881dd226c9973118d0819")
# a= u'Names': [u'/admiring_sinoussi'], u'Id': u'e77abb7717fc1a17c42c2e5a8607a858558684b80fc2c6316899a61956179444',
# cli.kill("4b806bcbbd3d487d0818bcbe32ce521f60a1608ce06881dd226c9973118d0819")


