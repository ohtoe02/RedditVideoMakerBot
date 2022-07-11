from django.shortcuts import render
from .models import SettingsLoader
from .serializers import SettingsLoaderSerializer
from os import linesep
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
class SettingsLoaderViewSet(viewsets.ModelViewSet):
    queryset = SettingsLoader.objects.all()
    serializer_class = SettingsLoaderSerializer
    
@api_view(['GET'])
def save_to_file(self):
    config = ''
    loader = SettingsLoader.objects.get(pk=1)
    dict_loader = loader.__dict__
    for key in list(dict_loader.keys())[2:]:
       config += f'{key.upper()}="{dict_loader[key]}"{linesep}' 
    with open('../../.env','w') as file:
        file.write(config)
    return Response({'Saved':'Sucsessfully'})
@api_view(['GET'])
def index(request):
        settings, created = SettingsLoader.objects.get_or_create(pk=1)
        return Response(SettingsLoaderSerializer(settings).data)