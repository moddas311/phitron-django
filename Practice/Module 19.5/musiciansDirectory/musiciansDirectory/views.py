from django.shortcuts import render,redirect
from album.models import Album


def home(request):
    albums=Album.objects.all().get()
    return render(request,'home.html',{'albums':albums})