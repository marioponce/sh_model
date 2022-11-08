#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.apps import AppConfig


class ModelMgmtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_mgmt'
