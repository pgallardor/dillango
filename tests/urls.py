from django.urls import path
from .views import *

urlpatterns = [
    path('tests/', json_list, name='json_list'),
    path('tests/single', single_json, name='single_json')
]