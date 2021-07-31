from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.



class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=15)
    mobile=models.CharField(max_length=10)


    
    


