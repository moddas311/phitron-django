from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def home(request):
    if request.method == 'POST':
        form=forms.ExampleForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form=forms.ExampleForm()
    return render(request,'home.html',{'form':form})