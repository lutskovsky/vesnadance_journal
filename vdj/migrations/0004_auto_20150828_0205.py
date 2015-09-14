# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdj', '0003_auto_20150828_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendedby',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='attendedby',
            name='student',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='students',
            field=models.ManyToManyField(to='vdj.Student', verbose_name='ученики'),
        ),
        migrations.DeleteModel(
            name='AttendedBy',
        ),
    ]
