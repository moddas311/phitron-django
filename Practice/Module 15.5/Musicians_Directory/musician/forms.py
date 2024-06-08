from .models import Musician
from django import forms 

class MusicianForm(forms.ModelForm):
    class Meta: 
        model = Musician
        fields='__all__'