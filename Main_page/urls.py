from django.urls import path
from . import view
urlpatterns = [
    path('home', view.home)
]