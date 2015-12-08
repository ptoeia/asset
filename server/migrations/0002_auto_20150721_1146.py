# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machines',
            name='srv_ip',
        ),
        migrations.RemoveField(
            model_name='machines',
            name='srv_location',
        ),
        migrations.RemoveField(
            model_name='machines',
            name='srv_name',
        ),
        migrations.RemoveField(
            model_name='machines',
            name='srv_purpose',
        ),
        migrations.RemoveField(
            model_name='machines',
            name='srv_remark',
        ),
        migrations.RemoveField(
            model_name='machines',
            name='srv_status',
        ),
        migrations.AddField(
            model_name='machines',
            name='ip',
            field=models.GenericIPAddressField(null=b'true', verbose_name=b'ip', blank=b'true'),
        ),
        migrations.AddField(
            model_name='machines',
            name='location',
            field=models.CharField(max_length=20, null=b'true', verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae', blank=b'true'),
        ),
        migrations.AddField(
            model_name='machines',
            name='name',
            field=models.CharField(max_length=20, null=b'true', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d', blank=b'true'),
        ),
        migrations.AddField(
            model_name='machines',
            name='purpose',
            field=models.CharField(max_length=30, null=b'true', verbose_name=b'\xe7\x94\xa8\xe9\x80\x94', blank=b'true'),
        ),
        migrations.AddField(
            model_name='machines',
            name='remark',
            field=models.CharField(max_length=40, null=b'true', verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=b'true'),
        ),
        migrations.AddField(
            model_name='machines',
            name='status',
            field=models.CharField(max_length=20, null=b'true', verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=b'true'),
        ),
    ]
