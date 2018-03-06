from django.db import models

# Create your models here.
class Telephone(models.Model):
     number = models.CharField(max_length=15,blank=True)
     score = models.IntegerField(default=0)

class Count(models.Model):
     count = models.IntegerField(default=0)
