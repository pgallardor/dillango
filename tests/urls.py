from django.urls import path
from .views import *

urlpatterns = [
    path('tests', json_list, name='json_list'),
    path('tests/single', single_json, name='single_json'),
    path('tests/upload', receive_file, name='receive_file'),
    path('tests/record', create_record, name='create_record'),
    path('tests/renderpdf', pdf_test, name='pdf_test')
]