from django.db import models

# Create your models here.
class Padre(models.Model):

    Papa = models.CharField(max_length=42)
    Edad = models.IntegerField(2)

class Madre(models.Model):

    Mama = models.CharField(max_length=42)
    Edad = models.IntegerField(2)

class Hermanos(models.Model):

    Hermanos = models.CharField(max_length=42)
    Edad = models.IntegerField(2)
