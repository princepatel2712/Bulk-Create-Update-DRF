from django.db import models


# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    speciality = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name
