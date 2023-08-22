# train_schedule/urls.py

from django.urls import path
from train_schedule import views

urlpatterns = [
    path('trains/', views.get_train_schedule, name='get_train_schedule'),
    path('register/', views.register_company, name='register_company'),
    path('get-auth-token/', views.get_authorization_token, name='get_authorization_token'),
]
