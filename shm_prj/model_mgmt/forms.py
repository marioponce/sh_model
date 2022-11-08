#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from .models import Farmer, Parcel


class FarmerForm(forms.ModelForm):
    """Farmer's form"""

    class Meta:
        model = Farmer 
        fields = [ # fields to be filled in the form
            'fName',
            'lName',
            'age',
            'sex'
        ]
        labels = { # labels to display in the form instead of the field names
            'fName': 'First Name',
            'lName': 'Last Name',
            'age': "Age",
            'sex': "Sex"
        }


class ParcelForm(forms.ModelForm):
    """Parcel's form"""

    class Meta:
        model = Parcel
        fields = [ # fields to be filled in the form
            'name',
            'lon',
            'lat',
            'storage',
            'grass',
            'fertility',
            'livestock',
            'capital',
            'income',
            'farmer'
        ]
        labels = { # labels to display in the form instead of the field names
            'name': "Place's name",
            'farmer': 'Owner'
        }
