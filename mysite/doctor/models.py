from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    age = models.IntegerField()
