from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Farmer(models.Model):
    """Farmer's class"""
    fName = models.CharField(max_length=40)
    lName = models.CharField(max_length=40)
    age = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(18)]
    )
    sex = models.CharField(
        max_length=1,
        choices=[('M', 'Male'), ('F', 'Famale')]
    )

    def __str__(self) -> str:
        """Return the name of the instance"""
        return self.fName + '_' + self.lName


class Parcel(models.Model):
    """Parcel's class"""
    name = models.CharField(max_length=40)
    lon = models.FloatField(
        validators=[MaxValueValidator(77.0), MinValueValidator(74.0)]
    )
    lat = models.FloatField(
        validators=[MaxValueValidator(21.0), MinValueValidator(18.0)]
    )
    storage = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    grass = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    fertility = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    livestock = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    capital = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    income = models.FloatField(
        validators=[MaxValueValidator(100.0), MinValueValidator(0.0)]
    )
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE,
                               related_name='parcels')

    def __str__(self) -> str:
        """Return the parcel's name"""
        return self.name
