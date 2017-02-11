# Create your views here.
# -*- coding:utf-8 -*-
# __author__ = 'abc'
import csv
import os, re
import json
import subprocess

from django.shortcuts import render_to_response
from django.forms.models import model_to_dict
#from django.core.servers.basehttp import FileWrapper

from server.models import Servers
from form import ServerForm,UserRegister

from function import pagination

from django.http import HttpResponseRedirect,HttpResponse,StreamingHttpResponse
from django.db.models import Q

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User


@login_required(login_url='login.html')
def index(request):
    return render_to_response('index.html')



@login_required(login_url='login.html')
def assets(request):  # display the server information and search function together
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']
        qset = (
             Q(ip__icontains=query)|
             Q(name__icontains=query)|
             Q(remark__icontains=query)|
             Q(purpose__icontains=query)
                  )
        server = Servers.objects.filter(qset)
        server_list, page_list = pagination(request, server)
        return render_to_response('asset.html', {'server_list': server_list, "page_list": page_list})
    server = Servers.objects.all()
    server_list,page_list = pagination(request,server)
    return render_to_response('asset.html',{'server_list': server_list, "page_list": page_list})

# add server
@login_required(login_url='login.html')
def add_server(request):
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect ( '/server/index' )
    else:
        form = ServerForm()
    return render_to_response ('add.html',{'form': form})


# edit server
@login_required(login_url='login.html')
def edit_server(request, eid):  # e_id is the server id to be edit
    sid = int(eid)
    edit_svr = Servers.objects.get(id=sid)
    if request.method == 'POST':
        edit_form = ServerForm(request.POST, instance=edit_svr)  # bound the instance with edit_form
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect('/server/index')
    else:
        edit_form = ServerForm(instance=edit_svr)
    return render_to_response('edit.html', {'edit_form': edit_form, 'sid': sid})

# delete server
@login_required(login_url='login.html')
def del_server(request, d_id):  # d_id is the server id to be delete
    server = Servers.objects.get(id=int(d_id))
    server.delete()
    return HttpResponseRedirect('/server/index')

# User Register
@login_required(login_url='login.html')
def user_register(request):
    if request.method == 'POST':
        newuser = UserRegister(request.POST)
        if newuser.is_valid():
            username = newuser.cleaned_data['username']
            email = newuser.cleaned_data['email']
            password = newuser.cleaned_data['password']
            User.objects.create_user(username,email,password)
            return HttpResponseRedirect('/server/manager')
    else:
        newuser = UserRegister()
    return render_to_response('register.html',{'newuser': newuser,})


# user login
def login_view(request):
    error = False
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                request.session['username'] = user.username
                return render_to_response('resource.html',{'username': username})
            else:
                error = True
    info = '用户名或密码不对'
    return render_to_response('login.html',{'error': error, 'info': info,})

@login_required(login_url='login.html')
def index(request):
    username = request.session.get('username','anybody')
    return render_to_response('index.html',{'username': username})

# logout
@login_required(login_url='login.html')
def logout_view(request):
    del request.session['username']
    logout(request)
    return HttpResponseRedirect('/server/')

# display admins
@login_required(login_url='login.html')
def user(request):
    admins = User.objects.all()
    return render_to_response('useradmin.html', {'admins': admins})



@login_required(login_url='login.html')
def manager(request):
    sessionid = request.COOKIES
    return render_to_response('manager.html',{'sessionid': sessionid})


@login_required(login_url='login.html')
def log(request):
    return render_to_response('log.html')

#@login_required(login_url='login.html')
def download(request, projectname): #log file download
    def  file_iterator(file_name,chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "F:\python_project\log\%s.zip" % projectname
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/x-zip-compressed'
    response['Content-Disposition'] = 'attachment;filename = %s.zip' % projectname
    return response


def server_info_update(request, id):
    try:
        server = Servers.objects.get(pk=int(id))
        raw_info = subprocess.check_output("/usr/bin/ansible {ip} -m setup".format(ip=server.private_ip),shell=True)
        base_info = json.loads(raw_info.split('=>')[1])['ansible_facts']
        server.cpu = base_info['ansible_processor_vcpus']
        server.memory = round(int(base_info['ansible_memtotal_mb'])/1024.0,1)
        disk_info = base_info['ansible_devices']
        server.disk_volume = sum([int(disk_info[disk]['sectors'])*int(disk_info[disk]['sectorsize'])  for disk in disk_info])/1024**3
        server.hostname = base_info['ansible_hostname']
        server.os = base_info['ansible_lsb']['description']
        server.save()
        feedback = u'更新成功'
    except:
       feedback =  u'更新失败'
    return HttpResponse(feedback)

def cmd_run(request):
    cmd = request.POST.get('cmd','')
    if cmd:
        result = subprocess.check_output("/usr/bin/ansible {ip} -raw -a '{cmd}'".format(ip,cmd),shell=True)
    
    return render_to_response('cmd_run.html')

def test(request):
    return render_to_response('bootstrap.html')