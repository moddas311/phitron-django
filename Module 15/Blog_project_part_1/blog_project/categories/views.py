from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_category(request):
    if request.method == 'POST': #user post request korche
       category_form = forms.CategoryForm(request.POST)  #user er post request data eikhane capture korlam
       if category_form.is_valid(): # post kora data gula valid kina amra check kortechi
           category_form.save() # jodi data gula valid hoy taile data databse e save hbe
           return redirect('add_category') # sob thik thakle user k redirect kore category page e redirect kortechi
    else: #user normally website e gele blanck page pabe
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form': category_form})