from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import UpdateView
import requests
import json

# Create your views here.
def index(request):
    pass


def callapigetmethod(request):
    url='http://127.0.0.1:8000/API/list/'
    head={'Content-Type': 'application/json'}

    res= requests.get(url, headers=head)

    print(res.json())
    print(res.status_code)
    return HttpResponse('done')
