#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, {'template_name': 'catalog/index.html'},
        'catalog_home'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.show_category,
        {'template_name': 'catalog/category.html'}, 'catalog_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.show_product,
        {'template_name': 'catalog/product.html'}, 'catalog_product'),
]
