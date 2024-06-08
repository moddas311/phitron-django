from django.shortcuts import render
from musician.models import Musician

def home(request):
    musician_data = Musician.objects.all()
    print(musician_data)
    return render(request,'home.html',{'data': musician_data})