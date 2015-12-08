# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_mactest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mactest',
            name='location',
            field=models.CharField(max_length=20, null=b'true', verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae', blank=b'false'),
        ),
    ]
