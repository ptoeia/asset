# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20150723_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(max_length=20, null=b'true', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d'),
        ),
    ]
