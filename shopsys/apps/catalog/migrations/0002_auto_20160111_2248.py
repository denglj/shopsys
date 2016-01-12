# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(verbose_name='是否激活', default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='名称', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Slug', unique=True, help_text='根据name生成的，用于生成页面URL，必须唯一'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(verbose_name='品牌', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(verbose_name='图片', max_length=50, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(verbose_name='设为激活', default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_bestseller',
            field=models.BooleanField(verbose_name='标为畅销', default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(verbose_name='标为推荐', default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.CharField(help_text='meta 描述标签', max_length=255, verbose_name='Meta描述'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(help_text='meta 关键词标签, 逗号分隔', max_length=255, verbose_name='Meta关键词'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(verbose_name='旧价格', decimal_places=2, max_digits=9, blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(verbose_name='价格', decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(verbose_name='计量单位', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(verbose_name='Slug', unique=True, max_length=255, help_text='根据name生成的，用于生成页面URL，必须唯一'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
    ]
