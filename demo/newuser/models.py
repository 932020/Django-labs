from django.db import models

# Create your models here.

class Myuser(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=30)
    email= models.EmailField(max_length=20)
    password = models.CharField(max_length=12)

