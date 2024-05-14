from django import forms
from .models import Movies


class Movie_form(forms.ModelForm):
    class Meta: 
        fields = ["title"]
        model = Movies



