from django.urls import path
from . import views

urlpatterns = [
    path('all_sessions/', views.sessions, name='all_sessions'),
]
