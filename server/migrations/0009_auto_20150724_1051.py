# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_mactest_location'),
    ]

    operations = [
#        migrations.DeleteModel(
#            name='mactest',
#        ),
#        migrations.AlterField(
#            model_name='machine',
#            name='ip',
#            field=models.GenericIPAddressField(protocol=b'ipv4', unique=b'true', verbose_name=b'ip'),
#        ),
        migrations.AlterField(
            model_name='machine',
            name='location',
            field=models.CharField(blank=b'true', max_length=20, null=b'true', verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae', choices=[(b'binjiang', '\u6ee8\u6c5f\u673a\u623f'), (b'gongsi', '\u516c\u53f8\u673a\u623f'), (b'jiaxing', '\u5609\u5174\u673a\u623f')]),
        ),
    ]
