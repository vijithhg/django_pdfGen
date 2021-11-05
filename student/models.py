from django.db import models
from django.db.models.base import Model

# Create your models here.



class StudentDetails(models.Model):

    CATEGORY = (
        ('CS','CS'),
        ('Science','Science'),
        ('Humanities','Humanities')
    )

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    course = models.CharField(max_length=50, choices=CATEGORY)
    mobile = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name