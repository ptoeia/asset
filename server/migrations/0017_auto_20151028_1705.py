# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_auto_20151028_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machine',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='machine',
            name='location',
            field=models.CharField(blank=b'true', max_length=20, null=b'true', verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae', choices=[(b'\xe6\xbb\xa8\xe6\xb1\x9f\xe6\x9c\xba\xe6\x88\xbf', '\u6ee8\u6c5f\u673a\u623f'), (b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x9c\xba\xe6\x88\xbf', '\u516c\u53f8\u673a\u623f'), (b'\xe5\x98\x89\xe5\x85\xb4\xe6\x9c\xba\xe6\x88\xbf', '\u5609\u5174\u673a\u623f')]),
        ),
    ]
