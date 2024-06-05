
from django.urls import path
# from .views import contact
from . import views

urlpatterns = [
    path("courses/", views.courses),
    path("", views.first_app_home),
    path("about/", views.about),
]
