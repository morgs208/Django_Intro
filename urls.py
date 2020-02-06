from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("new", views.new),
    path("create", views.create),
    path("edit/<number>/", views.edit),
    path("destroy", views.destroy),
    path("<number>", views.show),
    
