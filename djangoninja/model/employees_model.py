from django.db import models

from .departments_model import Departments
from .jobs_model import Jobs
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    hire_date = models.DateField()
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    manager = models.ForeignKey("self", on_delete=models.SET_NULL,null=True,blank=True)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.id) +"-" + self.first_name + " " + self.last_name
                + " Job title: " + self.job.title)