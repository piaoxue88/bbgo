# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-12 03:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='paper-files/%Y-%m-%d/')),
                ('content_type', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('5completed', '\uacb0\uc7ac\uc644\ub8cc'), ('3rejected', '\ubc18\ub824'), ('2progress', '\uacb0\uc7ac\uc911'), ('4canceled', '\ucde8\uc18c'), ('1proposed', '\uae30\uc548')], default='1proposed', max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=41)),
                ('content', models.TextField()),
                ('comment', models.CharField(blank=True, default='', max_length=1024)),
                ('approved', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('approved_at', models.DateTimeField(auto_now_add=True)),
                ('cancelmsg', models.CharField(blank=True, default='', max_length=1024)),
                ('completed', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_approver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('comment', models.CharField(blank=True, default='', max_length=1024)),
                ('approved', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('approved_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='paper',
            name='cc',
            field=models.ManyToManyField(blank=True, default='', related_name='paper_cc', to='papers.Person'),
        ),
        migrations.AddField(
            model_name='paper',
            name='files',
            field=models.ManyToManyField(blank=True, to='papers.Attachment'),
        ),
        migrations.AddField(
            model_name='paper',
            name='notifiers',
            field=models.ManyToManyField(blank=True, default='', related_name='paper_notifiers', to='papers.Person'),
        ),
        migrations.AddField(
            model_name='paper',
            name='supporters',
            field=models.ManyToManyField(blank=True, related_name='paper_supporters', to='papers.Support'),
        ),
        migrations.AddField(
            model_name='paper',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
