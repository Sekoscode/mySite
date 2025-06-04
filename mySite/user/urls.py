# yourapp/urls.py
from django.urls import path
from .views import CustomLogoutView
from user import views

urlpatterns = [
    # Other URL patterns
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
