from django.shortcuts import render
#from rest_framework.request import Request
from .models import Trainee
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@api_view(['GET'])

def index(request):
    doc ={
        '/' : 'overview',
        '/list': 'return collection of trainee',
    }
    return Response(doc)
###### List ##########
@api_view(['GET'])

def List(request, id=0):
    Trainee.objects.create(name="eman",branch=2)
    if (id == 0):
        trainees = Trainee.objects.all()
        if (trainees is not None):
            data = Traineeser(trainees, many=True)
            print(data.data)
        return Response(data.data)

    else:
        trainee = Trainee.objects.get(id=id)
        if (trainee is not None):
            data = Traineeser(trainee)
        return Response(data.data)
############ Insert ########

@api_view(['POST'])

def create(request):
    print(request.data['name'])
    t = Traineeser(**request.data)
    if(t.is_valid()):
        t.save()
        return Response(t.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


#################### Update ##########
@api_view(['PUT'])
def Update(request):
    t = Traineeser(request.data)
    t.save()
    return Response(status=status.HTTP_200_OK)

############## Delete ########
@api_view(['DELETE'])

def Delete(request):
    return Response(status=status.HTTP_200_OK)




