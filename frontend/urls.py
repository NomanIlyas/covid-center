from django.urls import path
from . import views

urlpatterns = [
    path('importStates/', views.importStates ),
    path('importCountries/', views.importCountries ),
]