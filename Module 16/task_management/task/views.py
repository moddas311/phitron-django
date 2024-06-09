from django.shortcuts import render, redirect
from .models import Task
from . forms import TaskForm

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        addTask = TaskForm(request.POST)
        if addTask.is_valid():
            addTask.save()
            return redirect('add_task')
    else:
        addTask = TaskForm()
    return render(request,'task.html',{'form': addTask})


def edit_task(request,id):
    taskObject = Task.objects.all().get(pk=id)
    addTask = TaskForm(instance = taskObject)
    if request.method == 'POST':
        addTask =TaskForm(request.POST,instance = taskObject)
        if addTask.is_valid():
            addTask.save()
            return redirect('add_task')
    return render(request,'task.html', {'form': addTask})


def delete_task(request,id):
    taskObject = Task.objects.all().get(pk=id).delete()
    return redirect('home')