from django.db import models


# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    theme = models.CharField(max_length=250)
    synopsis = models.CharField(max_length=500)


class User(models.Model):
    objects = None
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.email
