from django.shortcuts import render, redirect
from . import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
       register_form = forms.RegistrationForm(request.POST) 
       if register_form.is_valid():
           register_form.save()
           messages.success(request, 'Account Created Successfully...!')
           return redirect('home')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'signup.html', {'form': register_form, 'type': 'Register'})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            login_form = AuthenticationForm(request=request,data = request.POST)
            if login_form.is_valid():
                 name=login_form.cleaned_data['username']
                 login_pass = login_form.cleaned_data['password']
                 user = authenticate(username=name , password = login_pass)
                 if user is not None:
                    messages.success(request, 'Logged in Successfully...!')
                    login(request,user)
                    return redirect('profile')
        else:
          login_form = AuthenticationForm()
        return render(request,'login.html',{'form': login_form})
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
           user_form = forms.ChangeUserData(request.POST,instance=request.user)
           if user_form.is_valid():
            user_form.save()
            messages.success(request,"You successfully Updated your profile")
            return redirect('profile')
        else:
           user_form = forms.ChangeUserData(instance = request.user)
        return render(request,'profile.html',{'form':user_form})
    else:
        return redirect('login')
    

def pass_change(request):
    if request.method == 'POST':
       form = PasswordChangeForm(request.user, data = request.POST) 
       if form.is_valid():
           form.save()
           messages.success(request, 'Password updated Successfully...!')
           update_session_auth_hash(request, form.user)
           return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'pass_change.html', {'form': form})

    
def user_logout(request):
    logout(request)
    messages.error(request, 'Logged out Successfully...!')
    return redirect('profile')