from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    name = models.CharField(max_length=40)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    