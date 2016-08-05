#coding: utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse,render_to_response
from django.shortcuts import redirect

def login(request):
    #如果是get请求
    #如果是POST,检验用户输入
    print request.method
    if request.method == 'POST':
        input_email = request.POST['email']
        input_pwd = request.POST['pwd']
        if input_email == 'rain@qq.com' and input_pwd == "123":
            return redirect("http://www.qingyidai.com")
            #return redirect("/son/")
        else:
            return render(request,'login.html',{'status':'用户名或密码错误!'})
    return render(request,'login.html')

def index(request):
    #数据库取数据
    #数据和HTML渲染
    from app01 import models
    if request.method == "POST":
        #添加数据
        input_em = request.POST['em']
        input_pw = request.POST['pw']
        #models.UserInfo.objects.create(email=input_em,pwd=input_pw)   //添加
        #models.UserInfo.objects.filter(email=input_em).delete()       //删除
        #models.UserInfo.objects.filter(email=input_em).update(pwd='999')   //修改

    #获取UserInfo表中所有数据
    user_info_list = models.UserInfo.objects.all()
    #user_info_list列表，列表的元素 #一行；email,pwd
    return render(request,'index.html',{'user_info_list':user_info_list})

def son(request):
    return render(request,'son1.html')

# Create your views here.
def home(request):
    #return HttpResponse('ok')
    #找到home.html
    #读取html,返回给用户
    dic = {'name':'ALEX','age':19,}
    #user_list = ['Rain','Alex']
    return render(request, 'home.html',dic,)
