from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import UpdateView

# Create your views here.
from ..trainee2.models import Trainee


def index(request):
    trainees = Trainee.objects.all()
    return HttpResponse(trainees)


