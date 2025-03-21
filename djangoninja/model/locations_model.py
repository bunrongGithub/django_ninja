from django.db import models

from djangoninja.model.countries_model import Countries


class Locations(models.Model):
    street_address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.ForeignKey(
        Countries, on_delete=models.CASCADE, related_name="countries"
    )
