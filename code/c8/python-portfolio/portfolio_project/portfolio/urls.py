from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('about', views.about, name='about'),
    # Add paths for other pages
]
