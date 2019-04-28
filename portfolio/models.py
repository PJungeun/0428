from django.db import models

# Create your models here.

class Person(models.Model):

    name = models.CharField( max_length=200)
    age = models.IntegerField()
    major = models.CharField(max_length=200)
    grade = models.IntegerField()
    hometown = models.CharField(max_length=200)