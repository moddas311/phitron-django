from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import registration
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class Registration(CreateView):
    model=User
    form_class=registration
    template_name='signup.html'
    success_url=reverse_lazy('login')
  
  

class log_in(LoginView):
    template_name='login.html'
    
    def form_valid(self,form):
        messages.success(self.request,'you logged successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,'your logged information is wrong')
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(*kwargs)
        context['type']='Login'
        return context
    
@method_decorator(login_required,name='dispatch')
class log_out(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')

