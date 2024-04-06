from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Movies
from .forms import Movies_form



def index(request):
    return HttpResponse("test")



class Form_movies(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = Movies_form(self.request.POST or None)
        # if ctx["form"].is_valid():
        #     ctx["title"] = ctx["form"].title
            # ctx["res"] = Movies.objects.get(title=ctx["form"].title)
        return ctx