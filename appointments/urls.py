from django.urls import path
from .views import create_appointment, list_appointments, create_busy_hour, list_busy_hours

app_name = 'appointments'

urlpatterns = [
    path('create/', create_appointment, name='create'),
    path('list/', list_appointments, name='list'),
    path('busy/create/', create_busy_hour, name='busy_create'),
    path('busy/list/', list_busy_hours, name='busy_hours_list'),
]
