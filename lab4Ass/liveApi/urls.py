from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('overview' , index),
    path('list', List),
    path('list/<int:id>', List),
    path('insert', create),
    path('update',Update),
    path('delete',Delete),

]
