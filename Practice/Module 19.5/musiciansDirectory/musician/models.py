from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    instrument_type = models.CharField(max_length = 70)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name