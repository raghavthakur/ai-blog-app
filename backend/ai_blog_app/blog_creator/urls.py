from django.urls import path
from . import views

# List of all URLs for app
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('signup', views.user_signup, name='signup'),
]
