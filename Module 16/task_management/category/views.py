from django.shortcuts import render, redirect
from .forms import CategoryForm

# Create your views here.
def add_category(request):
    if request.method == "POST":
        addCategoryForm = CategoryForm(request.POST)
        if addCategoryForm.is_valid():
            addCategoryForm.save()
            return redirect('add_category')
    else:
        addCategoryForm = CategoryForm()

    return render(request,'category.html',{'form': addCategoryForm})