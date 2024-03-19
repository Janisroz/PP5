from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form for creating a session post
    """
    class Meta:
        model = Post
        fields = ('description', 'session', 'session_rating',)
        widgets = {
            'session_rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }
