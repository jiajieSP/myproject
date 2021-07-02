from django.db import models

# Create your models here.
class Model (models.Model):
    modelName = models.CharField(max_length=30)
    modelDate = models.CharField(max_length=30)
    modelDesc = models.CharField(max_length=30)

class Student(models.Model):   
    roll = models.CharField(max_length=100)
    sclass = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    class Meta:
        db_table = "students"