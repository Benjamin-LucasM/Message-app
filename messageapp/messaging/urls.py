from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('register/', views.register, name='register'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('<str:username>/', views.chat, name='chat'),
]