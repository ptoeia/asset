# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.admin import User

# create table machine
class Servers (models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=20, verbose_name='主机名', help_text=u'必填')
    public_ip = models.GenericIPAddressField(max_length=30, verbose_name='公网ip',  protocol='ipv4')
    private_ip = models.GenericIPAddressField(max_length=30, verbose_name='内网ip', help_text=u'必填',unique='true', protocol='ipv4')
    os = models.CharField(max_length=20, verbose_name='操作系统', default='Centos6.4')
    cpu = models.PositiveSmallIntegerField(verbose_name='cpu', default=1)
    memory = models.PositiveIntegerField(verbose_name='内存', default=1024)
    disk_volume = models.PositiveIntegerField(verbose_name='硬盘容量', default=60)
    purpose = models.CharField(max_length=30, verbose_name='用途', null='true', blank='true')
    location = models.CharField(max_length=30, verbose_name='位置', null='true', blank='true', choices=(('CDN机房','CDN机房'),('公司机房','公司机房')))
    status = models.CharField(max_length=20, verbose_name='状态', null='true', blank='true', choices=(('on', 'on'),('off', 'off')))
    remark = models.CharField(max_length=40, verbose_name='备注', null='true', blank='true')

    def __unicode__(self):
        return self.hostname

    class Meta:
         db_table = 'servers'


# create table user

