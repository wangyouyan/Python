# coding:utf-8
from dwebsocket import  *
from  api import  *
import  json
import threading
import time

mydocker = Docker_manage()
from  docker import *
url = "tcp://172.16.13.38:2375"
cli = Client(base_url=url)



@accept_websocket
def index(request):
    # print request.is_websocket()
    # print dir(request.websocket)
    # message = request.websocket.wait()
    # stats_obj = cli.stats("4b806bcbbd3d487d0818bcbe32ce521f60a1608ce06881dd226c9973118d0819")
    # stats_obj = cli.stats("test01")
    # request.websocket.send("s")
    all = cli.containers()
    all_dic = {}
    for i in all:
        all_dic[i["Names"][0].replace("/","")]= cli.stats(i["Id"])

    while True:
        new_list = []
        new_dict = {}
        for k,v in all_dic.items():
            for i in v:
                a = json.loads(i)
                # print k,a
                new_dict[k] = a
                break
        new_str = json.dumps(new_dict)
        # print new_str
        request.websocket.send(new_str)
        if all_dic.__len__()==0:
            print "no container "
            time.sleep(1)
            all = cli.containers()
            if(all):
                all_dic = {}
                for i in all:
                    all_dic[i["Names"][0].replace("/", "")] = cli.stats(i["Id"])
                continue
            else:
                request.websocket.send("0")





    # for  message in request.websocket:
    #     message = message.lower()
    #     print type(message)

        # for i in stats_obj:
            # a = json.loads(i)
            # request.websocket.send(i)
        # print message




