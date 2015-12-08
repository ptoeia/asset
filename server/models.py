# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.admin import User

# create table machine
class Machine (models.Model):
    name = models.CharField(max_length=20, verbose_name='主机名', help_text=u'必填')
    ip = models.GenericIPAddressField(max_length=30, verbose_name="ip", unique='true', protocol='ipv4')
    purpose = models.CharField(max_length=30, verbose_name='用途', null='true', blank='true')
    status = models.CharField(max_length=20, verbose_name='状态', null='true', blank='true',choices=(('on', 'on'),('off', 'off')))

    remark = models.CharField(max_length=40, verbose_name='备注', null='true', blank='true')

    def __unicode__(self):
        return self.name

    class Meta:
         ordering = ['name']


# create table user
class User(models.Model):
    username = models.CharField(max_length=50, unique='true')
    password = models.CharField(max_length=50)
    email = models.EmailField(unique='true')

    def __unicode__(self):
        return self.username
