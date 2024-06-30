from django.urls import path
from . import views

urlpatterns=[
    path('edit_musician/<int:id>', views.editMusicianView.as_view(),name='edit_musician'),
    path('add_musician/', views.addMusicianView.as_view(),name='add_musician'),
]