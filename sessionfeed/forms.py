from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    """
    Form for creating a session post
    """
    class Meta:
        model = Post
        fields = ('description','session','session_rating',)
