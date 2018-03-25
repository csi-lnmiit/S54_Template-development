# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_gym_gym_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(max_length=40, null=True)),
                ('city', models.CharField(max_length=40, null=True)),
                ('complete_add', models.CharField(max_length=100, null=True)),
                ('google_maps_add', models.CharField(max_length=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content_Long',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail1', models.CharField(max_length=100, null=True)),
                ('detail2', models.CharField(max_length=100, null=True)),
                ('detail3', models.CharField(max_length=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('purpose', models.CharField(max_length=100, null=True)),
                ('specs', models.CharField(max_length=100, null=True)),
                ('complete', models.CharField(max_length=200, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='photos',
            name='Photo_id',
        ),
        migrations.AddField(
            model_name='gym',
            name='charges',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='contact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='timing',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='photos',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='content_short',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='gym_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Gym'),
        ),
        migrations.AddField(
            model_name='content_long',
            name='gym_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Gym'),
        ),
        migrations.AddField(
            model_name='address',
            name='gym_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Gym'),
        ),
    ]