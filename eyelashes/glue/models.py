from django.db import models

class Glue(models.Model):
    modelname = models.CharField(max_length=100)
    content = models.CharField(max_length=10)  # Allowing input like "25ml", adjust max_length as needed
    count = models.IntegerField()
