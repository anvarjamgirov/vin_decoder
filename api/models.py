from django.db import models


class VIN(models.Model):
    vin_code = models.CharField(
        max_length=63,
        unique=True
    )
    make = models.CharField(
        max_length=511
    )
    model = models.CharField(
        max_length=511
    )
    year = models.CharField(
        max_length=7
    )
    manufacturer = models.CharField(
        max_length=127
    )
    engine = models.CharField(
        max_length=127
    )
    trim = models.CharField(
        max_length=63
    )
    transmission = models.CharField(
        max_length=63
    )

    def __str__(self):
        return self.model
