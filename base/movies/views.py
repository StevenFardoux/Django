from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Movies
from .forms import Movies_form
import requests


def index(request):
    return HttpResponse("test")



class Form_moviesView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = Movies_form(self.request.GET or None)
        return ctx
    

class Form_validate(TemplateView):
    template_name = "request.html"
    api_key = "8a4b62b2"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = Movies_form(self.request.GET or None) 
        if ctx["form"].is_valid():
            ctx["title"] = ctx["form"].cleaned_data['title']  
            template_name = "request.html"

            ctx["movies"] = Movies.objects.filter(title=ctx["title"])
            if not ctx["movies"]:
                # Appel API et sauvegarde dans la base de données
                res = requests.get(f"http://www.omdbapi.com/?apikey={self.api_key}&t={ctx['title']}")
                movie_data = res.json()

                movie = Movies(title=movie_data['Title'], year=movie_data['Year'], genre=movie_data['Genre'])
                movie.save()
                ctx["movies"] = [movie]
            print(ctx["movies"])
        return ctx

    
    