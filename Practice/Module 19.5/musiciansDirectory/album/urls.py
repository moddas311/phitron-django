from django.urls import path
from . import views

urlpatterns = [
    path('add_album/',views.addAlbumView.as_view(),name='add_album'),
    path('edit_album/<int:id>',views.updateAlbumView.as_view(),name='edit_album'),
    path('delete_album/<int:id>',views.deleteAlbumView.as_view(),name='delete_album'),
]