# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='machines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('srv_name', models.CharField(max_length=20)),
                ('srv_ip', models.GenericIPAddressField()),
                ('srv_purpose', models.CharField(max_length=30)),
                ('srv_status', models.CharField(max_length=20)),
                ('srv_location', models.CharField(max_length=20)),
                ('srv_remark', models.CharField(max_length=40)),
            ],
        ),
    ]
