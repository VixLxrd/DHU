from django.db import models


class Home(models.Model):
    address = models.PositiveIntegerField()
    date = models.PositiveIntegerField()
    aqua_hot = models.PositiveIntegerField()
    aqua_cold = models.PositiveIntegerField()
    el = models.PositiveIntegerField()
    temp = models.PositiveIntegerField()
