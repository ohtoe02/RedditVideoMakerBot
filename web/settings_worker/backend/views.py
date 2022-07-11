from django.shortcuts import render
from .models import SettingsLoader
from .serializers import SettingsLoaderSerializer
from rest_framework import viewsets
class SettingsLoaderViewSet(viewsets.ModelViewSet):
    queryset = SettingsLoader.objects.all()
    serializer_class = SettingsLoaderSerializer
