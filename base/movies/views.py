from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Movies
from .forms import Movie_form
import requests


def index(request):
    return HttpResponse("test")



class Form_moviesView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = Movie_form(self.request.GET or None)
        return ctx
    

class Form_validate(TemplateView):
    template_name = "request.html"
    api_key = "8a4b62b2"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = Movie_form(self.request.GET or None) 
        if ctx["form"].is_valid():
            ctx["title"] = ctx["form"].cleaned_data['title']  
            print("leel", ctx["title"])
            movies = Movies.objects.filter(title__icontains=ctx["title"])
            
            if not movies:
                # Call API and save in DB
                resMovies = requests.get(f"https://www.omdbapi.com/?apikey={self.api_key}&s={ctx['title']}")
                print(resMovies.content)
                if resMovies.status_code == 200:
                    movies_data = resMovies.json()

                    for movie_data in movies_data["Search"]:
                        resGenre = requests.get(f"https://www.omdbapi.com/?apikey={self.api_key}&i={movie_data["imdbID"]}")
                        if resGenre.status_code == 200:
                            genres_date = resGenre.json()

                            movie = Movies(title=movie_data['Title'], year=movie_data['Year'], genre=genres_date['Genre'])
                            movie.save()
            ctx["movies"] = Movies.objects.filter(title__icontains=ctx["title"])
            print(ctx["movies"])
        return ctx

    
    