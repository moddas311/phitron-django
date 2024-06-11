from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('pass_change/', views.change_pass, name='pass_change'),
    path('pass_change2/', views.change_pass2, name='pass_change2'),
]
