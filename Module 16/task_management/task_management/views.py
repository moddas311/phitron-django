from django.shortcuts import render
from task.models import Task
def home(request):
    tasks=Task.objects.all()
    return render(request,'home.html',{'tasks': tasks})