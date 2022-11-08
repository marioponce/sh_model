#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Farmer, Parcel
from .forms import FarmerForm, ParcelForm


def home(request):
    """Renders the home site."""
    return render(request, 'model_mgmt/home.html')


def farmers(request):
    """Renders the list of farmers in the database."""
    farmers = Farmer.objects.all()  # gets all the farmers instances
    context = {'farmers': farmers}
    return render(request, 'model_mgmt/farmers.html', context)


def add_farmer(request):
    """Calls the FarmerForm and adds a farmer instance to the db."""
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmers')
    else:
        form = FarmerForm()

    context = {'form': form}
    return render(request, 'model_mgmt/add_farmer.html', context)


def delete_farmer(request, farmer_id):
    """Deletes a specific farmer instance from the db."""
    farmer = Farmer.objects.get(id=farmer_id)
    farmer.delete()
    return redirect('farmers')


def edit_farmer(request, farmer_id):
    """Calls the FarmerForm and edits a specific farmer instance to the db."""
    farmer = Farmer.objects.get(id=farmer_id)
    if request.method == 'POST':
        form = FarmerForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('farmers')
    else:
        form = FarmerForm(instance=farmer)

    context = {'form': form}
    return render(request, 'model_mgmt/edit_farmer.html', context)


def parcels(request):
    """Renders the list of parcels in the database."""
    parcels = Parcel.objects.all()
    context = {'parcels': parcels}
    return render(request, 'model_mgmt/parcels.html', context)


def add_parcel(request):
    """Calls the ParcelForm and adds a parcel instance to the db."""
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parcels')
    else:
        form = ParcelForm()

    context = {'form': form}
    return render(request, 'model_mgmt/add_parcel.html', context)


def delete_parcel(request, parcel_id):
    """Deletes a specific parcel instance from the db."""
    parcel = Parcel.objects.get(id=parcel_id)
    parcel.delete()
    return redirect('parcels')


def edit_parcel(request, parcel_id):
    """Calls the ParcelForm and edits a specific parcel instance to the db."""
    parcel = Parcel.objects.get(id=parcel_id)
    if request.method == 'POST':
        form = ParcelForm(request.POST, instance=parcel)
        if form.is_valid():
            form.save()
            return redirect('parcels')
    else:
        form = ParcelForm(instance=parcel)

    context = {'form': form}
    return render(request, 'model_mgmt/edit_parcel.html', context)
