# tours/models.py

from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    dates = models.DateField()
    capacity = models.IntegerField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
