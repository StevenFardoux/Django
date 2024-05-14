from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Movies
from .forms import Movies_form



def index(request):
    return HttpResponse("test")



class Form_moviesView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = Movies_form(self.request.GET or None)
        if ctx["form"].is_valid():
            ctx["title"] = ctx["form"].cleaned_data['title']    
            template_name = "request.html"
        return ctx
    

class Form_validate(TemplateView):
    template_name = "request.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = Movies_form(self.request.GET or None) 
        if ctx["form"].is_valid():
            ctx["title"] = ctx["form"].cleaned_data['title']    
            template_name = "request.html"
        return ctx

    
    