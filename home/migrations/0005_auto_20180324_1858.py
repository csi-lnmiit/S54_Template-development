# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-24 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180324_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo_id', models.IntegerField()),
                ('gym_id', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='gym',
            old_name='text',
            new_name='content_short',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='image',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='width_field',
        ),
        migrations.AddField(
            model_name='gym',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='gym',
            name='gym_id',
            field=models.IntegerField(null=True),
        ),
    ]