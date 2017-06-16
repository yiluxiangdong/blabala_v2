from django.shortcuts import render,render_to_response

# Create your views here.
def index(request):
    # if request.method=='POST' and request.POST:
    #     name = request.POST['username']
    #     passwd = request.POST['password']
    #     print name,passwd

    return render_to_response('login.html',locals())

def register(request):

    return render_to_response('monitor_register.html',locals())