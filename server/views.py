# Create your views here.
# -*- coding:utf-8 -*-
# __author__ = 'abc'
import csv

from django.shortcuts import render_to_response
from django.forms.models import model_to_dict
from django.core.servers.basehttp import FileWrapper

from server.models import Machine
from form import ServerForm,UserRegister,pagination

from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User



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
        server = Machine.objects.filter(qset)
        server_list, page_list = pagination(request, server)
        return render_to_response('index.html', {'server_list': server_list, "page_list": page_list})
    server = Machine.objects.all()
    server_list,page_list = pagination(request,server)
    return render_to_response('index.html',{'server_list': server_list, "page_list": page_list})

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
    edit_svr = Machine.objects.get(id=sid)
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
    server = Machine.objects.get(id=int(d_id))
    server.delete()
    return HttpResponseRedirect('/server/index')

# User Register
@login_required(login_url='/templates/login.html')
def user_register(request):
    if request.method == 'POST':
        newuser = UserRegister(request.POST)
        if newuser.is_valid():
            username = newuser.cleaned_data['username']
            email = newuser.cleaned_data['email']
            password = newuser.cleaned_data['password']
            newuser = User.objects.create_user(username,email,password)
#           NewUser.save()
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
                #request.session['username'] = username
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
    # del request.session['username']
    logout(request)
    return HttpResponseRedirect('/server/')

# display admins
@login_required(login_url='login.html')
def manager(request):
    admins = User.objects.all()
    return render_to_response('manager.html', {'admins': admins})

# display link resource
@login_required(login_url='login.html')
def link(request):
    return render_to_response('resource.html')

#
#def export_to_csv(request):
#    response = HttpResponse(content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="csv"'
    #write =csv.wirter(response)
#    csv_data = (
#        ('first row','foo','bar','baz'),
#        ('second row','a','b','c','"testing"',"here's a quota"),
#    )
#    return render_to_response('csv',{'data': csv_data})












