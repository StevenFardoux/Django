from django.urls import path

from . import views

urlpatterns = [
    path("", views.Form_moviesView.as_view(), name="index"),
    path("search/", views.Form_validate.as_view(), name="request"),

]