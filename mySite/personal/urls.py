from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about_me/', views.online_shop),
    path('vision_board/', views.vision_board),
]