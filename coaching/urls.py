from django.urls import path
from . import views

urlpatterns = [
    path('all_sessions/', views.sessions, name='all_sessions'),
    path('all_coaches/', views.coaches, name='all_coaches'), 
    path('<int:session_id>/', views.session_detail, name='session_detail'),
]
