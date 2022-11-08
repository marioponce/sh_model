#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Farmer(models.Model):
    """Farmer's class"""
    # first and last name are limited to 40 chars
    fName = models.CharField(max_length=40) # first name
    lName = models.CharField(max_length=40) # last name
    # age should be between 18 and 100
    age = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(18)]
    )
    # sex should be binary: M or F
    sex = models.CharField(
        max_length=1,
        choices=[('M', 'Male'), ('F', 'Female')]
    )

    def __str__(self) -> str:
        """Return the name of the instance"""
        return self.fName + '_' + self.lName


class Parcel(models.Model):
    """Parcel's class"""
    #  name are limited to 40 chars
    name = models.CharField(max_length=40)
    #longitude and latitude should be in the area of Maharashtra, India
    lon = models.FloatField(
        validators=[MaxValueValidator(77.0), MinValueValidator(74.0)]
    )
    lat = models.FloatField(
        validators=[MaxValueValidator(21.0), MinValueValidator(18.0)]
    )
    # storage is a float between 0 and 100
    storage = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    # grass is a float between 0 and 100
    grass = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    # fertility is a float between 0 and 100
    fertility = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    # livestock is a float between 0 and 100
    livestock = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    # capital is a float between 0 and 100
    capital = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    # income is a float between 0 and 100
    income = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    # We stablis a relationship one to many with the class farmer
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE,
                               related_name='parcels')

    def __str__(self) -> str:
        """Return the parcel's name"""
        return self.name
