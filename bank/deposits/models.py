from django.db import models

# Create your models here.
class Deposit(models.Model):
    deposit = models.FloatField()
    term = models.IntegerField()
    rate = models.FloatField()
    interest = models.FloatField()

