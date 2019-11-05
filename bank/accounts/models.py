from django.db import models
from django.utils import timezone

class Account(models.Model):
    owner = models.CharField(max_length=40)
    balance = models.FloatField()
    creation_date = models.DateField(auto_now_add=True)
