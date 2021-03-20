from django.db import models


class Home(models.Model):
    city = models.SmallIntegerField()
    adress = models.SmallIntegerField()
    date = models.SmallIntegerField()
    temp = models.SmallIntegerField()
    aqua_cold = models.FloatField()
    aqua_hot = models.FloatField()
    el = models.SmallIntegerField()
