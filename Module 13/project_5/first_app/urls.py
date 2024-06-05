from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    # path('django_form/', views.djangoContactForm, name='django_form'),
    # path('django_form/', views.studentForm, name='django_form'),
    path('django_form/', views.PasswordValidation, name='django_form'),
]