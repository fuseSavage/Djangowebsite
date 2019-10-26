from django.shortcuts import render
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl

from .models import Service
from .models import Service3

# Create your views here.
def services(req):
    if req.method == 'POST':
        post = req.POST
        s = Service()
        s.icon = post['icon']
        s.title = post['title']
        s.detail = post['detail']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/services.html', { 'services': services })
    else:
        print('ร้องขอทำมะดา')
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/services.html', { 'services': services })

def index(req):
    if req.method == 'POST':
        post = req.POST
        s = Service3()
        s.name = post['name']
        s.lname = post['lname']
        s.email = post['email']
        s.comments = post['comments']
        s.save()
        services = Service3.objects.all()
        print(services)
        return render(req, 'linuxapp/index.html', { 'services': services })

    else:
        print('ร้องขอทำมะดา')
        services = Service3.objects.all()
        print(services)
        return render(req, 'linuxapp/index.html', { 'services': services })

def developer(req):
    return render(req, 'linuxapp/developer.html')

