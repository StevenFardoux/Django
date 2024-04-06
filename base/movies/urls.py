from django.urls import path

from . import views

urlpatterns = [
    path("", views.Form_movies.as_view(), name="index"),
    #path("/tt", views.index, name="test"),

]