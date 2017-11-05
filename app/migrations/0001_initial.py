# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-04 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True, verbose_name='\u5de5\u5177\u540d')),
                ('Description', models.TextField(default='', verbose_name='\u7b80\u4ecb')),
                ('Size', models.CharField(max_length=200, verbose_name='\u5927\u5c0f')),
                ('Link', models.FileField(default='', upload_to='toolbox', verbose_name='\u4e0b\u8f7d\u5730\u5740')),
                ('Instructions', models.FileField(upload_to='tools/', verbose_name='\u4f7f\u7528\u624b\u518c')),
                ('Time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='ToolType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=32, unique=True, verbose_name='tooltype')),
            ],
        ),
        migrations.AddField(
            model_name='tool',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ToolType'),
        ),
    ]