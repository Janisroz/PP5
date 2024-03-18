from django import forms
from products.widgets import CustomClearableFileInput
from .models import Coach


class CoachForm(forms.ModelForm):
    """
    Form to create and edit Coaches
    """

    class Meta:
        model = Coach
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'img-border mb-2'
