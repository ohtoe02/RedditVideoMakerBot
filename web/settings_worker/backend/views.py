import subprocess
from os import linesep
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get(request):
    response = {}
    with open('../../.env', 'r') as file:
        for line in file.read().splitlines():
            data = line.split('=')
            response[data[0].lower()] = data[1].replace('"', '')
        return Response(response)


@api_view(['PUT'])
def update(request):
    config = ''
    for key in list(request.data.keys()):
        template = f'"{request.data[key]}"' if type(request.data[key]) is str or type(
            request.data[key]) is bool else f'{request.data[key]}'
        config += f'{key.upper()}={template}\n'
    with open('../../.env', 'w') as file:
        file.write(config)
    subprocess.call("../../main.py", shell=True)
    return Response({'Saved': 'Successfully'})
