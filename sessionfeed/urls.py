from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_feed, name='session_feed'),
    path('delete/<int:session_id>/', views.delete_post, name='delete_post'),
]
