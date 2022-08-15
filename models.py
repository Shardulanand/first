from distutils.command.upload import upload
from email.mime import image
from django.db import models

class Food(models.Model):
    name= models.CharField(max_length=250)
    price= models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='Food Image/')

    def __str__(self):
        return self.name
        


