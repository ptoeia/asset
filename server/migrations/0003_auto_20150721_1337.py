# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20150721_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=b'true', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d', blank=b'true')),
                ('ip', models.GenericIPAddressField(null=b'true', verbose_name=b'ip', blank=b'true')),
                ('purpose', models.CharField(max_length=30, null=b'true', verbose_name=b'\xe7\x94\xa8\xe9\x80\x94', blank=b'true')),
                ('status', models.CharField(max_length=20, null=b'true', verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=b'true')),
                ('location', models.CharField(max_length=20, null=b'true', verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae', blank=b'true')),
                ('remark', models.CharField(max_length=40, null=b'true', verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=b'true')),
            ],
        ),
        migrations.DeleteModel(
            name='machines',
        ),
    ]
