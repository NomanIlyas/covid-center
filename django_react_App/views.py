import generics as generics
from django.db import models
from rest_framework import generics,serializers
from .models import Lead, LeadSerializer

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer