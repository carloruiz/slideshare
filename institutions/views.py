from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    with open('institutions/data/institutions.json') as f:
        institutions = f.read()
  
    response = HttpResponse(institutions, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response
