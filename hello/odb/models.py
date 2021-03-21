from django.db import models


class Home(models.Model):
    city = models.PositiveIntegerField()
    street = models.PositiveIntegerField()
    house = models.PositiveIntegerField()
    flat = models.PositiveIntegerField()
    date = models.PositiveIntegerField()
    aqua_hot = models.FloatField()
    aqua_cold = models.FloatField()
    el = models.PositiveIntegerField()
    temp = models.PositiveIntegerField()
