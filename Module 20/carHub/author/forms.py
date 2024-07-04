from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
# from .models import commnetsModel

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'id':'required'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'id':'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
class userChangeForm(UserChangeForm):
    password = None
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'id':'required'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'id':'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']