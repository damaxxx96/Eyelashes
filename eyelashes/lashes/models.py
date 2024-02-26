from django.db import models



class Lashes(models.Model):
    modelname = models.CharField(max_length=100)
    length = models.CharField(max_length=20)  # Allowing input like "5.5 cm", adjust max_length as needed
    width = models.CharField(max_length=20)   # Allowing input like "5.5 cm", adjust max_length as needed
    count = models.IntegerField()
