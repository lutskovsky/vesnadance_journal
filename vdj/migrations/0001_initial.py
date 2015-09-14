# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('standard_teacher_fee', models.IntegerField(default=1500, verbose_name='оплата преподавателя')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField(verbose_name='дата')),
                ('revenue', models.IntegerField(default=0, verbose_name='выручка')),
                ('rent', models.IntegerField(default=0, verbose_name='аренда')),
                ('comment', models.TextField(verbose_name='комментарий')),
                ('group', models.ForeignKey(null=True, verbose_name='группа', to='vdj.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='имя')),
                ('has_discount', models.BooleanField(default=False, verbose_name='право на скидку')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='имя')),
                ('groups', models.ManyToManyField(to='vdj.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='название')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='students',
            field=models.ManyToManyField(to='vdj.Student'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teachers',
            field=models.ManyToManyField(through='vdj.Fee', verbose_name='преподаватели', to='vdj.Teacher'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='venue',
            field=models.ForeignKey(to='vdj.Venue'),
        ),
        migrations.AddField(
            model_name='fee',
            name='lesson',
            field=models.ForeignKey(to='vdj.Lesson'),
        ),
        migrations.AddField(
            model_name='fee',
            name='teacher',
            field=models.ForeignKey(to='vdj.Teacher'),
        ),
    ]
