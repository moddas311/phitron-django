from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.home, name='category_wise_post'),
    path('author/', include('author.urls')),
    path('category/', include('categories.urls')),
    path('post/', include('posts.urls')),
]

from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)