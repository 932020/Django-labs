from django.db import models

# Create your models here.


class Course(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=50, null= True)

    def __str__(self):
        return self.name





class Trainee(models.Model):
    id = models.AutoField(primary_key = True)
    name= models.CharField(max_length=50 , null= True)
    branch = models.IntegerField( null= True)
    courses = models.ForeignKey(Course,on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.name







