from django.db import models
class Regions(models.Model):
    name = models.CharField(max_length=100)