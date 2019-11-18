from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    