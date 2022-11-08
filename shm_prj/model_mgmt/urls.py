#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('farmers/', views.farmers, name='farmers'),
    path('add_farmer/', views.add_farmer, name='add_farmer'),
    path('delete_farmer/<int:farmer_id>/',
         views.delete_farmer, name='delete_farmer'),
    path('edit_farmer/<int:farmer_id>/', views.edit_farmer, name='edit_farmer'),
    path('parcels/', views.parcels, name='parcels'),
    path('add_parcel/', views.add_parcel, name='add_parcel'),
    path('delete_parcel/<int:parcel_id>/',
         views.delete_parcel, name='delete_parcel'),
    path('edit_parcel/<int:parcel_id>/', views.edit_parcel, name='edit_parcel'),
]
