from django.db import models

# Create your models here.
class level(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name

class photo(models.Model):
    pname=models.CharField(max_length=250)
    pimg=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.pname
