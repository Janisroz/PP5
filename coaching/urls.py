from django.urls import path
from . import views

urlpatterns = [
    path('all_sessions/', views.sessions, name='all_sessions'),
    path('all_coaches/', views.coaches, name='all_coaches'),
    path('add_coach/', views.add_coach, name='add_coach'),
    path('delete/<int:coach_id>/', views.delete_coach, name='delete_coach'),
    path('<int:session_id>/', views.session_detail, name='session_detail'),
]
