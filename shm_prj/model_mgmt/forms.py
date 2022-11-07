from django import forms
from .models import Farmer, Parcel


class FarmerForm(forms.ModelForm):
    """Farmer's form"""

    class Meta:
        model = Farmer 
        fields = [
            'fName',
            'lName',
            'age',
            'sex'
        ]
        labels = {
            'fName': 'First Name',
            'lName': 'Last Name',
            'age': "Age",
            'sex': "Sex"
        }


class ParcelForm(forms.ModelForm):
    """Parcel's form"""

    class Meta:
        model = Parcel
        fields = [
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
        labels = {
            'name': "Place's name",
            'farmer': 'Owner'
        }
