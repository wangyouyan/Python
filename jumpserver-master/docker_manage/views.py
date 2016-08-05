# coding=utf-8
from django.http import StreamingHttpResponse
from django.shortcuts import render
# Create your views here.
from jumpserver.api import *
from api import  *
from forms import   *
import models

@require_role('admin')
def docker_index(request):
    mydocker = Docker_manage()
    header_title, path1, path2 = u'Docker概况', u'Docker管理', u'Docker概况'

    docker_host_count = mydocker.host_count
    all_docker_count = mydocker.all_docker_count
    active_docker_count = mydocker.get_active_docker-mydocker.get_paused_docker
    paused_docker_count = mydocker.get_paused_docker
    restarting_docker_count = mydocker.get_restarting_docker
    stop_docker_count =mydocker.get_stop_docker
    docker_image_count = mydocker.docker_image_count
    # print all_docker_count
    # print active_docker_count
    # print paused_docker_count
    # print stop_docker_count
    # print restarting_docker_count
    return  my_render('docker/docker_index.html',locals(),request)



# list docker info
@require_role('admin')
def  docker_list(request):
    mydocker = Docker_manage()
    docker_host = request.GET.get("docker_host","all")
    node = docker_host
    mydocker = Docker_manage()
    all_docker = mydocker.all_docker_host
    # print all_docker
    host_list =  all_docker.keys()
    if docker_host!="all":
        new_docker = []
        all_docker = mydocker.get_dockers(docker_host)
        for docker in all_docker:
            docker["docker_host"]=docker_host
            new_docker.append(docker)
        all_docker = new_docker
    else:
        new_docker = []
        for k,v in all_docker.items():
            for docker in v :
                docker["docker_host"]=k

                new_docker.append(docker)
        all_docker = new_docker
    # print docker_host
    # for i in all_docker:
    #     print i["Ports"]
    # contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)
    header_title, path1, path2 = u'Docker列表', u'Docker管理', u'Docker列表'
    return  my_render('docker/docker_list.html',locals(),request)

@require_role('admin')
def docker_host(request):
    if request.method == "GET":
        # docker_host_form = docker_conf_form()
        # print docker_host_form
        docker_status_list = []
        docker_hosts = models.docker_conf.objects.all()

        for i in docker_hosts:
            try:
                cli = Client(i.base_url)
                cli.images()
            except:
                docker_status_list.append('Error')
            else:
                docker_status_list.append("Ok")
        # print docker_status_list
        header_title, path1, path2 = u'Docker主机列表', u'Docker管理', u'Docker主机列表'
        return  my_render('docker/docker_host.html',locals(),request)
@require_role('admin')
def docker_host_add(request):
    if request.method == "GET":
        docker_host_form = docker_conf_form()
        header_title, path1, path2 = u'Docker主机添加', u'Docker管理', u'Docker主机添加'
        return my_render('docker/docker_host_add.html',locals(),request)
    else:
        docker_host_form = docker_conf_form(request.POST)
        print docker_host_form
        if docker_host_form.is_valid():
            docker_host_form.save()
            return HttpResponseRedirect(reverse('docker_host'))
        else:
            return my_render('docker/docker_host_add.html',locals(),request)

@require_role('admin')
def docker_host_del(request):
    # print "fuck"
    docker_host_ids = request.GET.get("id","")
    type= request.GET.get("type","")
    docker_host_list = docker_host_ids.split(',')
    print docker_host_list
    try:
        for docker_host_id in docker_host_list:
            docker_conf.objects.filter(id=docker_host_id).delete()
    except Exception as e :
        print e
        if type=="single":
            return HttpResponseRedirect(reverse('docker_host'))
        return  HttpResponse("False")
    if type == "single":
        return HttpResponseRedirect(reverse('docker_host'))
    return HttpResponse("True")


@require_role('admin')
def docker_connect_test(request):
    if request.method=="GET":
        docker_host = request.GET.get('host_name')
        base_url = request.GET.get('base_url')
        print base_url
        try:
            cli= Client(base_url)
            cli.images()
        except Exception as e :
            print e
            return HttpResponse("ERROR")
        return HttpResponse("True")

@require_role('admin')
def docker_host_edit(request):
    docker_host_id = request.GET.get('id', '')
    docker_host = get_object(docker_conf, id=docker_host_id)
    if request.method == "GET":
        # docker_host_id = request.GET.get('id','')
        host_name = request.GET.get('host_name','')

        edit_form = docker_conf_form(instance=docker_host)
        print edit_form
        return my_render('docker/docker_host_edit.html',locals(),request)
    else:
        edit_form = docker_conf_form(request.POST,instance=docker_host)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('docker_host'))
        else:
            return my_render('docker/docker_host_edit.html',locals(),request)


@require_role('admin')
def docker_edit(request):
    if request.method == "GET":
        edit_form = docker_edit_form()
        docker_name = request.GET.get("docker_name")
        docker_id = request.GET.get("id")
        docker_host = request.GET.get("docker_host")
        # print docker_name
        return  my_render("docker/docker_edit.html",locals(),request)
    else:
        docker_name = request.POST.get("old_name")
        docker_new_name = request.POST.get("docker_name")
        docker_host = request.POST.get("docker_host")
        mydocker = Docker_manage()
        print docker_name
        mydocker.rename_docker(docker_host,docker_name,docker_new_name)
        return HttpResponseRedirect(reverse("docker_list"))

@require_role('admin')
def docker_image_list(request):
    mydocker = Docker_manage()
    docker_host =  request.GET.get("docker_host","all")
    query =  request.GET.get("query",None)
    node = docker_host
    mydocker =Docker_manage()
    all_docker_images = mydocker.all_docker_images
    # print all_docker_images
    host_list =  all_docker_images.keys()
    if docker_host!="all":
        all_docker_images = mydocker.get_docker_images(docker_host)
        if query:
            return HttpResponse(json.dumps(all_docker_images))
    else:
        new_docker_images = []
        for k,v in all_docker_images.items():
            for docker in v :
                docker["docker_host"]=k
                new_docker_images.append(docker)

        all_docker_images = new_docker_images
    print all_docker_images
    header_title, path1, path2 = u'Docker镜像列表', u'Docker管理', u'Docker镜像列表'
    return my_render('docker/docker_image_list.html',locals(),request)

@require_role('admin')
def create_docker(request):
    mydocker = Docker_manage()
    if request.method == "GET":
        docker_form =  create_container()
        header_title, path1, path2 = u'创建Docker容器', u'Docker管理', u'创建Docker容器'
        return my_render('docker/docker_create.html',locals(),request)
    else:
        container_name = request.POST.get("container_name")
        docker_host = request.POST.get("docker_host")
        image = request.POST.get("container_images")
        host_name = request.POST.get("host_name")
        mount_type = request.POST.get("mount_type", 'nomount')
        docker_mount = request.POST.get("docker_mount", None)
        volume_name = request.POST.get("volume_name", None)
        port_type = request.POST.get("port_type", None)
        if port_type=="default":
            port = None
        else:
            port = request.POST.get("port",None)

        volumes= None
        if mount_type == "auto":
            volumes = docker_mount
            volume_name = None
        elif mount_type == "input":
            volume_name = volume_name
            # if volume_name:
            #     volume_name = volume_name.replace("_data", "")
        elif mount_type == "nomount":
            pass
        command = request.POST.get("command")
        # print container_name ,docker_host,image,command
        print  mydocker.create_docker(docker_host,container_name,image,
                                      command,host_name,volume_name,
                                      docker_mount,volumes,port)
        return  HttpResponseRedirect(reverse("docker_list"))

@require_role('admin')
def operate_docker(request):
    mydocker = Docker_manage()
    if request.method=="GET":
        docker_id = request.GET.get("id",None)
        docker_host_list = request.GET.get("docker_host",None)
        operate = request.GET.get("operate",None)
        operate_status = []
        print docker_host_list
        print docker_id
        print operate
        if hasattr(mydocker,operate):
            operate = getattr(mydocker,operate)
            if docker_id:
                for index, docker in enumerate(docker_id.split(",")):
                    docker_host = docker_host_list.split(",")[index]
                    operate_status.append(operate(docker_host,docker))
        print  operate_status
        ret  = []
        for i in operate_status:
            if i != True:
                ret.append(i)
        if ret == []:
            ret = True
        print ret
        return HttpResponse(ret)

mydocker = Docker_manage()
@require_role('admin')
def remove_image(request):
    image_name = request.GET.get("image_name", None)
    docker_host = request.GET.get("docker_host", None)
    image_name = image_name.split(",")
    docker_host = docker_host.split(",")
    print image_name,docker_host
    for index,image in enumerate(image_name):
        mydocker.remove_image_in_docker_host(image,docker_host[index])
    return HttpResponse("true")


# add image from ..
@require_role('admin')
def search_image(request):

    if request.method == "GET":
        registry = request.GET.get("registry",None)
        search_name = request.GET.get("search_name",None)
        docker_host = request.GET.get("docker_host",None)
        print registry
        if registry:
            mydocker = Docker_manage()
            search_ret = mydocker.search_images(search_name,docker_host)
            print search_ret
            # print registry,search_name,docker_host

            ret_content = ""
            operate = '''
                <td class="text-center">
                    <div class="btn-group">
                      <button type="button" class="btn btn-primary" ><a style="color: whitesmoke" onclick="pull_image(this)">Pull</a></button>
                      <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <span class="caret"></span>
                      </button>
                      <ul class="dropdown-menu ">
                        <li><a value=""   class="operate_docker" >Other</a></li>
                      </ul>
                    </div>
                </td>
            '''

            continue_list = ["is_automated","is_trusted","star_count","is_official","registry_name"]
            for i in search_ret:
                content = ""
                ret_head = ""
                for k,v in i.items():
                    if k in continue_list:
                        continue
                    ret_head+="<th>%s</th>"%k
                    content += "<td class='%s'>%s</td>"%(k,str(v))
                ret_content+="<tr>%s%s</tr>"%(content,operate)
            ret_head += "<th>Operate</th>"

            ret_html = '<table class="table table-hover"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>'%(ret_head,ret_content)
            # print ret_html
            return HttpResponse(ret_html)
        else:
            images_form = pull_image_form()
            images_form.registry = "docker.io"
            images_form.search_name = "test"

            return my_render('docker/docker_image_pull.html',locals(),request)


@require_role('admin')
def pull_image(request):
    if request.method == "GET":
        image_name = request.GET.get("image_name",None)
        registry = request.GET.get("registry",None)
        docker_host = request.GET.get("docker_host",None)
        print docker_host
        mydocker.pull_image_from_name(image_name,docker_host)
        return HttpResponse("ok")


#  get  pull image history...
@require_role('admin')
def get_pull_image_progress(request):
    record = models.docker_image_pull_record.objects.filter(operate_user=request.user)
    detail = models.pull_image_detail.objects.select_related().filter(docker_image=record)
    a=[]
    for i in    detail:
        print  type(i.id)
        print type(i.progress)
        print type(i.total)
        item = i.id+i.status+i.docker_image.image_name
        print item
        a.append(str(item))
    print type(a)
    return HttpResponse(a)

@accept_websocket
def pull_image_progress(request):
    time.sleep(3)
    # mydocker = Docker_manage()
    mydocker.pull_image_progress(request)

@require_role('admin')
def volume_list(request):
    mydocker = Docker_manage()
    docker_host = request.GET.get("docker_host","all")
    query = request.GET.get("query",None)

    node = docker_host
    mydocker = Docker_manage()
    all_docker = mydocker.all_docker_host
    # print all_docker
    host_list =  all_docker.keys()
    all_volumes = mydocker.volume_list(docker_host)
    if query:
        choice = ()
        # for volume in all_volumes[docker_host]["Volumes"]:
        #     temp_choice = (volume["Name"],volume["Mountpoint"])
        #     choice += (temp_choice,)
        new_data = json.dumps(all_volumes[docker_host]["Volumes"])
        # print new_data
        return HttpResponse(new_data)
    # all_volumes = json.loads(all_volumes)
    new_volumes = []
    for host,host_volumes in all_volumes.items():
        print host_volumes["Volumes"]
        if host_volumes["Volumes"]==None:
            break
        for volume in host_volumes["Volumes"]:
            volume["docker_host"]=host
            new_volumes.append(volume)

    # contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)
    header_title, path1, path2 = u'volume列表', u'Docker管理', u'volume列表'
    return  my_render('docker/volume_list.html',locals(),request)

@require_role('admin')
def volume_create(request):
    if request.method == "POST":
        docker_host = request.POST.get("docker_host")
        volume_name = request.POST.get("volume_name")
        mydocker.create_volume(docker_host,volume_name)
        return HttpResponseRedirect(reverse("docker_volume_list"))
    else:
        volume_form = create_volume()
        return my_render('docker/docker_volume_create.html',locals(),request)
@require_role('admin')
def removre_volume(request):

    docker_host = request.GET.get("docker_host")
    volume_name = request.GET.get("volume_name")
    # print docker_host,volume_name
    volume_name = volume_name.split(",")
    docker_host = docker_host.split(",")
    for index,volume in enumerate(volume_name):
        mydocker.remove_volume(docker_host[index], volume)
    return HttpResponse("true")
