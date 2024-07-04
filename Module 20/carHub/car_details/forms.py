from .models import commentsModel
from django import forms


class commentsForm(forms.ModelForm):
    car = None
    class Meta:
        model = commentsModel
        exclude = ['car',]
        widget = {
            'body': forms.Textarea()
        }
    