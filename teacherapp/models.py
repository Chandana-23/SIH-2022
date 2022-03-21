from django.db import models
from django import forms
# Create your models here.

class Notifications(models.Model):
    file_id = models.TextField(primary_key=True)
    document = models.FileField(upload_to='media')
    description = models.TextField(default='')
    posted = models.DateTimeField( auto_now=True)

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    genre = models.CharField(max_length=500)

class Members(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField(max_length=254,primary_key=True,default='chandanasamineni23@gmail.com')
    pwd = models.CharField(max_length=250)

class Jobs(models.Model):
    job_id = models.IntegerField(primary_key=True,default=1)
    job_name = models.TextField()
