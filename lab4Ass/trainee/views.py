import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import json
from django.http import HttpResponse


# Create your views here.
@api_view(['GET'])
def overview(request):
    apiurl={
        'overview':'/',
        'list': 'list',

    }
    return Response(apiurl)


################
'''
@api_view(['POST'])
def update_trainees(request,pk):
    trainee = Trainee.objects.get(pk=pk)
    
'''

def view_trainees(request,id=0):
    print(request.query_params)
    if id!=0:
        trainees= Trainee.objects.filter(id= id)
    else:
        trainees = Trainee.onjects.all()

    if trainees:
        data = Traineeserializer(trainees, many= True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



def callapiget(request):
    url="http://127.0.0.1:8000/API/list"
    header={
        "Content-Type": "apllication/json"
    }

    result= requests.get(url=url,headers=header)
    print(result.json())
    if result.status_code==200:
        return HttpResponse("Successful")
    return HttpResponse("something went wrong")


def callapipost(request):
    url = "http://127.0.0.1:8000/API/insert"
    header = {
        "Content-Type": "apllication/json",
    }

    data={
        "name":"eman",
        "branch":"2"

    }
    result = requests.post(url=url,data=json.dumps(data), headers=header)
    print(result.json())
    if result.status_code == 200:
        return HttpResponse("Successful")
    return HttpResponse("something went wrong")






