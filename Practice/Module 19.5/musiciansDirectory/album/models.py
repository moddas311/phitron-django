from django.db import models
from musician.models import Musician
from datetime import datetime

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length = 100)
    musician = models.ForeignKey(Musician,on_delete = models.CASCADE, related_name = 'Album')
    release_date = models.DateTimeField(auto_now_add = datetime.now())
    choice = {
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    }
    rating = models.CharField(max_length = 5,choices = choice)
    def __str__(self):
        return self.name
