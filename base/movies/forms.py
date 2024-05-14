from django import forms
from .models import Movies


class Movies_form(forms.ModelForm):
    class Meta: 
        fields = ["title"]
        model = Movies


