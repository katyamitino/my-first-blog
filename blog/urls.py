from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^product_list/sort_by_name/$', views.product_list_order_by_name, name='product_list_order_by_name'),
    url(r'^product_list/sort_min_to_max/$', views.product_list_ascending_order, name='product_list_min_to_max'),
    url(r'^product_list/sort_max_to_min/$', views.product_list_descending_order, name='product_list_max_to_min'),
    url(r'^product/(?P<pk>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^product/new/$', views.product_new, name='product_new'),
    url(r'^product/(?P<pk>\d+)/edit/$', views.product_edit, name='product_edit'),
    url(r'^product_list/(?P<pk>\d+)/delete/$', views.product_delete, name='product_delete'),

    url(r'^client_list/$', views.client_list, name='client_list'),
    url(r'^client_list/(?P<pk>\d+)/$', views.client_detail, name='client_detail'),
    url(r'^client_list/new/$', views.client_new, name='client_new'),
    url(r'^client_list/(?P<pk>\d+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^client_list/(?P<pk>\d+)/delete/$', views.client_delete, name='client_delete'),

    url(r'^order_list/$', views.order_list, name='order_list'),
    url(r'^order_list/(?P<pk>\d+)/$', views.order_detail, name='order_detail'),
    url(r'^order_list/new/$', views.order_new, name='order_new'),
    url(r'^order_list/(?P<pk>\d+)/edit/$', views.order_edit, name='order_edit'),
    url(r'^order_list/(?P<pk>\d+)/delete/$', views.order_delete, name='order_delete'),

    url(r'^supplier_list/$', views.supplier_list, name='supplier_list'),
    url(r'^supplier_list/(?P<pk>\d+)/$', views.supplier_detail, name='supplier_detail'),
    url(r'^supplier_list/new/$', views.supplier_new, name='supplier_new'),
    url(r'^supplier_list/(?P<pk>\d+)/edit/$', views.supplier_edit, name='supplier_edit'),
    url(r'^supplier_list/(?P<pk>\d+)/delete/$', views.supplier_delete, name='supplier_delete'),


    url(r'^$', views.search_form, name='product_list'),
    url(r'^search_results/$', views.search, name='search_results'),

    url(r'^statistics/$', views.statistics, name='statistics'),

    url(r'^$', views.count_prod, name='count_prod'),

    url(r'^$', views.passport_form, name='product_list'),
    url(r'^passport/$', views.passport, name='passport'),
]
