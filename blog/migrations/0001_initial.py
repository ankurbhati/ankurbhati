# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(null=True, blank=True)),
                ('status', models.IntegerField(max_length=1, choices=[(0, b'Inactive'), (1, b'Activate'), (2, b'Deleted')])),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'blog_blog',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('status', models.IntegerField(max_length=1, choices=[(0, b'Inactive'), (1, b'Activate'), (2, b'Deleted')])),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('blog', models.ForeignKey(blank=True, to='blog.Blog', null=True)),
                ('created_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'blog_comment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'blog_category',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='category_id',
            field=models.ForeignKey(blank=True, to='blog.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog',
            name='created_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
