from django.db import models


class Area(models.Model):
    region = models.CharField(max_length=200)


class City(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class Home(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    levels = models.PositiveSmallIntegerField()
