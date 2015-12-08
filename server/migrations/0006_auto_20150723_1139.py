# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20150723_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='mactest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d', blank=b'true')),
                ('ip', models.CharField(max_length=30, null=b'true', verbose_name=b'ip')),
            ],
        ),
        migrations.AlterField(
            model_name='machine',
            name='ip',
            field=models.GenericIPAddressField(null=b'true', verbose_name=b'ip', blank=b'true'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(max_length=20, null=b'true', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d', blank=b'true'),
        ),
    ]
