from django.db import models


class Tweezer(models.Model):
    modelname = models.CharField(max_length=100)
    color = models.CharField(max_length=50)  # Assuming color names won't exceed 50 characters
    count = models.IntegerField()