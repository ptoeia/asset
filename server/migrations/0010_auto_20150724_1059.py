# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_auto_20150724_1051'),
    ]

    operations = [
#        migrations.DeleteModel(
#            name='mactest',
#        ),
#        migrations.AlterField(
#            model_name='machine',
#            name='ip',
 #           field=models.GenericIPAddressField(protocol=b'ipv4', unique=b'true', verbose_name=b'ip'),
#        ),
        migrations.AlterField(
            model_name='machine',
            name='status',
            field=models.CharField(blank=b'true', max_length=20, null=b'true', verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'on', b'on'), (b'off', b'off')]),
        ),
    ]
