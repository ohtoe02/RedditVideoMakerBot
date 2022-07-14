from urllib import response
from django.shortcuts import render
from os import linesep
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get(request):
    response={}
    with open('../../.env','r') as file:
        for line in file.read().splitlines():
            data=line.split('=')
            response[data[0].lower()]=data[1][1:-1]
        return Response(response)   
@api_view(['PUT'])
def update(request):
    config = ''
    for key in list(request.data.keys()):
       config += f'{key.upper()}="{request.data[key]}"{linesep}' 
    with open('../../.env','w') as file:
        file.write(config)
    return Response({'Saved':'Sucsessfully'})