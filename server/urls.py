#__author__ = 'abc'

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'server.views.login_view'),
    url(r'^index', 'server.views.assets'),
    url(r'^add', 'server.views.add_server'),
 #   url(r'^export', 'server.views.export',name='export_csv'),
    url(r'^edit/(?P<eid>\d+)/$', 'server.views.edit_server'),
    url(r'^link', 'server.views.link'),
 #   url(r'^edit', 'server.views.display_meta'),
    url(r'^register', 'server.views.user_register'),
    url(r'^logout','server.views.logout_view'),
 #   url(r'^boot','server.views.boot'),
    url(r'^manager','server.views.manager'),
    url(r'^del/(?P<d_id>\d+)/$', 'server.views.del_server'),
  ]
