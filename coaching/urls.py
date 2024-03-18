from django.urls import path
from . import views

urlpatterns = [
    path('all_sessions/', views.sessions, name='all_sessions'),
    path('all_coaches/', views.coaches, name='all_coaches'),
    path('add_coach/', views.add_coach, name='add_coach'),
    path('edit_coach/<int:coach_id>/', views.edit_coach, name='edit_coach'),
    path('delete_coach/<int:coach_id>/', views.delete_coach, name='delete_coach'),
    path('<int:session_id>/', views.session_detail, name='session_detail'),
    path('add_session/', views.add_session, name='add_session'),
    path('delete_session/<int:session_id>/', views.delete_session, name='delete_session'),
]
