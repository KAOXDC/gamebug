from django.urls import path
from .views import *

urlpatterns = [
    path('example', example_view, name= 'example'),
]