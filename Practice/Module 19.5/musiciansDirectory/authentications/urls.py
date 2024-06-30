from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views. Registration.as_view(),name = 'signup'),
    path('login/',views.log_in.as_view(),name = 'login'),
    path('logout/',views.log_out.as_view(),name = 'logout'),
    
]