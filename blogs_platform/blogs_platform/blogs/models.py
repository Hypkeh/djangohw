from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(max_length=30)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

class Messages(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    posting_date = models.DateTimeField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Subscibers(models.Model):
    subscriber = models.ForeignKey(Profile, on_delete=models.CASCADE)
