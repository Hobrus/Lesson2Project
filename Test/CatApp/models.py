from django.db import models


# Create your models here.

class Human(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
