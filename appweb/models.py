from django.db import models


# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    theme = models.CharField(max_length=250)
    synopsis = models.CharField(max_length=500)
