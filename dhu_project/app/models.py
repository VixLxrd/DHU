from django.db import models

class Home(models.Model):
    city = models.IntegerField()
    adress = models.IntegerField()
    date = models.IntegerField()
    temp = models.IntegerField()
    aqua_cold = models.FloatField()
    aqua_hot = models.FloatField()
    el = models.IntegerField()
