from django.db import models
class Jobs(models.Model):
    title = models.CharField(max_length=100)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
