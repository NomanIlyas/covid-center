import generics as generics
from django.db import models
from rest_framework import generics,serializers

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')


# Create your models here.
