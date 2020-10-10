from django.urls import path
from . import views

urlpatterns = [
    path('api/django_react_App/', views.LeadListCreate.as_view() ),
]