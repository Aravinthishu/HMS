from django.db import models

# Create your models here.

class ContactModels(models.Model):
    fullname=models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    message = models.TextField()
