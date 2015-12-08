# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_auto_20150723_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='mactest',
            name='status',
            field=models.CharField(max_length=20, null=b'true', verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=b'true'),
        ),
    ]
