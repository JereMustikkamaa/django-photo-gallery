from django import forms
from .models import Image
from django.core.validators import RegexValidator

class ImageForm(forms.ModelForm):
    subfolder = forms.CharField(required=False, validators=[RegexValidator('^\w+$', message="Subfolder name can only contain alphanumeric characters")])
    class Meta:
        model = Image
        fields = ['title', 'subfolder', 'image', 'private', 'description' ]


