# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='根据name生成的全局唯一值，用于生成页面URL', unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(max_length=255, verbose_name='Meta 关键词', help_text='meta关键词，有利于SEO， 用逗号分隔')),
                ('meta_description', models.CharField(max_length=255, verbose_name='Meta 描述', help_text='meta描述')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'categories',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, help_text='根据name生成的全局唯一值，用于生成页面URL', unique=True)),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('old_price', models.DecimalField(max_digits=9, decimal_places=2, default=0.0, blank=True)),
                ('image', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(max_length=255, help_text='meta 关键词标签, 逗号分隔')),
                ('meta_description', models.CharField(max_length=255, help_text='meta 描述标签')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]
