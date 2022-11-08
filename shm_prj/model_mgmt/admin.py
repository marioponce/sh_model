#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Farmer, Parcel

admin.site.register(Farmer)
admin.site.register(Parcel)
