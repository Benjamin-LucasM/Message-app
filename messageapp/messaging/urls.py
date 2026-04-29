from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('register/', views.register, name='register'),
    path('<str:username>/', views.chat, name='chat'),
]