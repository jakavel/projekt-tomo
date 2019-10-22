# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-10-16 12:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0013_auto_20190411_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='courses.Course')),
                ('students', models.ManyToManyField(blank=True, related_name='course_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
