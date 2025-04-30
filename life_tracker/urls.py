from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tracker/', views.tracker, name='tracker'),
    path('review/', views.review, name='review'),
]
