from django import forms
from products.widgets import CustomClearableFileInput
from .models import Coach, Session
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CoachForm(forms.ModelForm):
    """
    Form to create and edit Coaches
    """

    class Meta:
        model = Coach
        fields = '__all__'

    description = forms.CharField(widget=SummernoteWidget())
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'img-border mb-2'


class SessionForm(forms.ModelForm):
    """
    Form to create and edit Sessions
    """

    class Meta:
        model = Session
        fields = '__all__'

    description = forms.CharField(widget=SummernoteWidget())
    exercises = forms.CharField(widget=SummernoteWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'img-border mb-2'
