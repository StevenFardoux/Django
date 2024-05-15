from django import forms
from .models import Movies


class Movie_form(forms.ModelForm):
    class Meta: 
        fields = ["title"]
        model = Movies

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Search movie"

