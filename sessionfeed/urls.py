from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_feed, name='session_feed'),
]
