from django.conf.urls import *
from . import views
from django.urls import path, re_path

app_name = 'Realestate'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customer/create/', views.customer_new, name='customer_new'),
    path('property_list', views.property_list, name='property_list'),
    path('property/create/', views.property_new, name='property_new'),
    path('property/<int:pk>/edit/', views.property_edit, name='property_edit'),
    path('property/<int:pk>/delete/', views.property_delete, name='property_delete'),
    path('liens_list', views.liens_list, name='liens_list'),
    path('liens/<int:pk>/edit/', views.liens_edit, name='liens_edit'),
    path('liens/<int:pk>/delete/', views.liens_delete, name='liens_delete'),
    path('liens/create/', views.liens_new, name='liens_new'),
]

