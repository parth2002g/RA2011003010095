# train_schedule_project/urls.py

from django.contrib import admin
from django.urls import path, include
from train_schedule import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('train_schedule.urls')),
    
]
