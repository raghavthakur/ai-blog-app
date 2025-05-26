from django.urls import path
from . import views

# List of all URLs for app
urlpatterns = [
    path('', views.index, name='index'),
]
