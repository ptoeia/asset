#-*- coding:utf-8 -*-
from django.core.paginator import Paginator,InvalidPage,EmptyPage

def pagination(request, server):  # pagination
    paginator = Paginator(server, 7)  # show 7 severs per page
    pagerange = paginator.page_range  # page list
    try:
        leaf = int(request.GET.get('page', '1'))
    except ValueError:
        leaf = 1
    try:
        server_list = paginator.page(leaf)
    except(EmptyPage,InvalidPage):
        server_list = paginator.page(paginator.num_pages)
    return server_list,pagerange