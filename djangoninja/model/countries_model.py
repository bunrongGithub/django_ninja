from django.db import models

from djangoninja.model.regions_model import Regions

class Countries(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE,related_name='countries')