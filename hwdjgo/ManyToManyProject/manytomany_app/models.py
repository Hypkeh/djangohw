from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=30)
    age = models.IntegerField()
    courses = models.ForeignKey('Course', on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=30)