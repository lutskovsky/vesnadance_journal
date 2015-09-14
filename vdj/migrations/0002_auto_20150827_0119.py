# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaughtBy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fee', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'преподаватели',
                'verbose_name': 'преподаватель',
            },
        ),
        migrations.RemoveField(
            model_name='fee',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='fee',
            name='teacher',
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': 'группы', 'verbose_name': 'группа'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name_plural': 'занятия', 'verbose_name': 'занятие'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'ученики', 'verbose_name': 'ученик'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': 'преподаватели', 'verbose_name': 'преподаватель'},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'verbose_name_plural': 'залы', 'verbose_name': 'зал'},
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='groups',
        ),
        migrations.AddField(
            model_name='group',
            name='teachers',
            field=models.ManyToManyField(to='vdj.Teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='venues',
            field=models.ManyToManyField(to='vdj.Venue'),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(verbose_name='номер телефона', default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='comment',
            field=models.TextField(verbose_name='комментарий', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teachers',
            field=models.ManyToManyField(to='vdj.Teacher', through='vdj.TaughtBy'),
        ),
        migrations.DeleteModel(
            name='Fee',
        ),
        migrations.AddField(
            model_name='taughtby',
            name='lesson',
            field=models.ForeignKey(to='vdj.Lesson'),
        ),
        migrations.AddField(
            model_name='taughtby',
            name='teacher',
            field=models.ForeignKey(to='vdj.Teacher'),
        ),
    ]
