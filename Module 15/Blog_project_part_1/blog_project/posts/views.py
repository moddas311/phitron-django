from django.shortcuts import render, redirect
from . import forms
from .import models

# Create your views here.
def add_post(request):
    if request.method == 'POST': #user post request korche
       post_form = forms.PostForm(request.POST)  #user er post request data eikhane capture korlam
       if post_form.is_valid(): # post kora data gula valid kina amra check kortechi
           post_form.save() # jodi data gula valid hoy taile data databse e save hbe
           return redirect('add_post') # sob thik thakle user k redirect kore category page e redirect kortechi
    else: #user normally website e gele blanck page pabe
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})

def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    post_form = forms.PostForm(instance = post)
    print(post.title)
    if request.method == 'POST': #user post request korche
       post_form = forms.PostForm(request.POST, instance=post)  #user er post request data eikhane capture korlam
       if post_form.is_valid(): # post kora data gula valid kina amra check kortechi
           post_form.save() # jodi data gula valid hoy taile data databse e save hbe
           return redirect('home') # sob thik thakle user k redirect kore category page e redirect kortechi
    
    return render(request, 'add_post.html', {'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')