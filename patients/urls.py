from django.urls import path
from .views import create_patient, list_patients, create_examination_record

app_name = 'patients'

urlpatterns = [
    path('create/', create_patient, name='create'),
    path('list/', list_patients, name='list'),
    path('create_examination/', create_examination_record, name='create_examination'),
]
