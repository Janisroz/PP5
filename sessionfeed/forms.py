from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Post



class PostForm(forms.ModelForm):
    """
    Form for creating a session post
    """
    # session_rating = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'id': 'id_session_rating'}),
    #     validators=[MinValueValidator(0), MaxValueValidator(5)],
    #     label='Session Rating (Must be between 1-5)'
    # )

    # class Meta:
    #     model = Post
    #     fields = ('description','session','session_rating',)

    class Meta:
        model = Post
        fields = ('description', 'session', 'session_rating',)
        widgets = {
            'session_rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }