from statistics import mode
from django.db import models

# Create your models here.
class Posts(models.Model):
    title=models.TextField()
    cover=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title

class Uploadedimg(models.Model):
    name=models.CharField('name',max_length=50)
    img=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name