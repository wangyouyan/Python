from django.shortcuts import render,HttpResponse,render_to_response


# Create your views here.

def login(request):
    #return HttpResponse('Welcome to Oldboy!')
    return render_to_response('login.html')

