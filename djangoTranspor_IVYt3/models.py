from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50, blank=False, null=False)
    county = models.CharField(max_length=50, default='Nairobi')
    destination = models.CharField(max_length=50, default='Nairobi')
    amount = models.CharField(max_length=50, blank=False, default=1)
    vehicle = models.CharField(max_length=50, blank=False, null=False)


def __str__(self):
    return self.name
