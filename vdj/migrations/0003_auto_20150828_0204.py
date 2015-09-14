# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdj', '0002_auto_20150827_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendedBy',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.RenameField(
            model_name='group',
            old_name='standard_teacher_fee',
            new_name='teacher_fee',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='students',
            field=models.ManyToManyField(to='vdj.Student', verbose_name='ученики', through='vdj.AttendedBy'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='venue',
            field=models.ForeignKey(verbose_name='зал', to='vdj.Venue'),
        ),
        migrations.AlterField(
            model_name='taughtby',
            name='fee',
            field=models.IntegerField(verbose_name='гонорар'),
        ),
        migrations.AlterField(
            model_name='taughtby',
            name='lesson',
            field=models.ForeignKey(verbose_name='занятие', to='vdj.Lesson'),
        ),
        migrations.AlterField(
            model_name='taughtby',
            name='teacher',
            field=models.ForeignKey(verbose_name='преподаватель', to='vdj.Teacher'),
        ),
        migrations.AddField(
            model_name='attendedby',
            name='lesson',
            field=models.ForeignKey(verbose_name='занятие', to='vdj.Lesson'),
        ),
        migrations.AddField(
            model_name='attendedby',
            name='student',
            field=models.ForeignKey(verbose_name='ученик', to='vdj.Student'),
        ),
    ]
