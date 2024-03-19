from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    """
    Registers the Post Model in the admin panel
    """
    list_display = ('author', 'session')
    search_fields = ['author', 'sesion']
    list_filter = ('author', 'session')
