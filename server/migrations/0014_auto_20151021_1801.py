# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_auto_20150728_1651'),
    ]


    operations = [
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(default=b'host', max_length=20, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d'),
        ),
    ]
