from django.db import models


class Home(models.Model):
    city = models.SmallIntegerField()
    adress = models.SmallIntegerField()
    date = models.SmallIntegerField()
    temp = models.SmallIntegerField()
    aqua = models.SmallIntegerField()
    el = models.SmallIntegerField()
