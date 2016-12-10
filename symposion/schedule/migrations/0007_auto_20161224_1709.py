# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-24 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_schedule', '0006_room_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Track')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symposion_schedule.Day')),
            ],
            options={
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
            },
        ),
        migrations.RemoveField(
            model_name='room',
            name='track',
        ),
        migrations.AddField(
            model_name='track',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symposion_schedule.Room'),
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([('room', 'day')]),
        ),
    ]