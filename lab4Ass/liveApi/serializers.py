from rest_framework import serializers
from .models import *

class Traineeser(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ['name','branch']
