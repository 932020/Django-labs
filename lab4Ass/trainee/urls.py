from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('overview' , overview),
    path('getapi',callapiget),

]