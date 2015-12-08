# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_auto_20150724_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='mactest',
        ),
        migrations.AlterField(
            model_name='machine',
            name='ip',
            field=models.GenericIPAddressField(protocol=b'ipv4', unique=b'true', verbose_name=b'ip'),
        ),
    ]
