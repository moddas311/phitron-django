from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is first app Courses page")

def about(request):
    return HttpResponse("This is first app About page")

def first_app_home(request):
    return HttpResponse("This is First App")