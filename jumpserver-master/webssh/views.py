from django.shortcuts import render,HttpResponse
# Create your views here.
from jumpserver.api import *

def index(request):
    return render(request,"gateone.html")

def create_signature(secret, *parts):
    import hmac, hashlib
    hash = hmac.new(secret, digestmod=hashlib.sha1)
    for part in parts:
        hash.update(str(part))
    return hash.hexdigest()

def get_auth_obj(request):
    import time, hmac, hashlib, json
    user = request.user.username
    gateone_server = 'https://172.16.13.80:10443'
    secret = "MTY5ZWVjYmU0YmFiNGYzNDliYjQxYWY2YTg2MjllNDc0N"
    api_key = "ODdiN2QwZjI3OGUwNGQ4Njg2M2I5MTY3NTM1NTVjMWQyZ"
    authobj = {
        'api_key': api_key,
        'upn': "gateone",
        'timestamp': str(int(time.time() * 1000)),
        'signature_method': 'HMAC-SHA1',
        'api_version': '1.0'
    }
    my_hash = hmac.new(secret, digestmod=hashlib.sha1)
    my_hash.update(authobj['api_key'] + authobj['upn'] + authobj['timestamp'])

    authobj['signature'] = my_hash.hexdigest()
    auth_info_and_server = {"url": gateone_server, "auth": authobj}
    valid_json_auth_info = json.dumps(auth_info_and_server)
    #   print valid_json_auth_info
    return HttpResponse(valid_json_auth_info)


def host_connect(request):
    host_ip = request.GET.get('host',None)
    host_user = request.GET.get('user','root')
    host_port = request.GET.get('port',22)

    if host_port =="":host_port=22
    print host_port
    if not host_ip :
        return my_render('404.html',locals(),request)
    else:
        return my_render('gateone.html',locals(),request)

# http://www.gaosijun.com/blog/detail/?id=9#
