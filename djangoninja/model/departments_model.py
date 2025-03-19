from django.db import models

from djangoninja.model.locations_model import Locations

class Departments(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Locations,on_delete=models.CASCADE,related_name='departments')