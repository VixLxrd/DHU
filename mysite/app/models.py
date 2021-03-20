from django.db import models


class Home(models.Model):
    region = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    levels = models.PositiveSmallIntegerField()
