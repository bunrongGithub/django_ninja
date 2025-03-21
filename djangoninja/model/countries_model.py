from django.db import models

from djangoninja.model.regions_model import Regions


class Countries(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(
        Regions, on_delete=models.CASCADE, related_name="countries"
    )

    @staticmethod
    def raw_query():
        for country in Countries.objects.raw(" SELECT * FROM djangoninja_countries"):
            return country

    @staticmethod
    def regions(name):
        return Regions.objects.filter(countries__name=name)
