from django.db import models

# Create your models here.

from album.models import Album
class Musician(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 40)
    phone = models.CharField(max_length = 14)
    album = models.ForeignKey(Album, on_delete = models.SET_NULL, null=True)
    Instrument_type = models.CharField(max_length = 200)
    
    def __str__(self) -> str:
        return self.name