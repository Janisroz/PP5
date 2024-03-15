from django.contrib import admin
from .models import Coach, Session
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Coach)
class CoachAdmin(SummernoteModelAdmin):
    """
    Registers the Coach Model in the admin panel
    """
    list_display = ('name', 'age')
    search_fields = ['name']
    list_filter = ('name', 'speciality')
    summernote_fields = ('description',)


@admin.register(Session)
class SessionAdmin(SummernoteModelAdmin):
    """
    Registers the Session Model in the admin panel
    """
    list_display = ('title', 'product', 'coach')
    search_fields = ['title', 'coach', 'product']
    list_filter = ('title', 'coach', 'product')
    summernote_fields = ('description', 'exercises',)