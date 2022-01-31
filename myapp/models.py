from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Student(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  date_of_birth = models.DateField()
  grade = models.IntegerField()
  phone = models.CharField(max_length=10)
  email = models.CharField(max_length=20, unique=True)