from django.urls import path 
from . import views 

urlpatterns=[
    path('signup/', views.signUpView.as_view(), name = 'signup'),
    path('login/', views.loginView.as_view(), name = 'login'),
    path('change/', views.change_pass, name = 'change'),
    path('logout/', views.logoutview.as_view(), name='logout'),
    path('profile/', views.profile, name = 'profile'),
    path('edit/<int:id>', views.update, name = 'update'),
]