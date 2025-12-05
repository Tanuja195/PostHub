from django.db import models
from django.utils import timezone
from django.urls import reverse

# To set author i.e. user from User Table we need to add below import *********
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField("thoughts",max_length=100,help_text='enter the title')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # possible values - auto_now = True , auto_now_add = True, default # need author having relation with Users table in Django Database
    author = models.ForeignKey(User,on_delete = models.CASCADE) # if user deleted, delete all the data

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Technical_Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) 

class Technical_Exercise(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) 

class Database_Structure(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) 
