from django.urls import path
from .views import create_medicine, list_medicines, update_medicine, delete_medicine

app_name = 'medicines'

urlpatterns = [
    path('create/', create_medicine, name='create'),
    path('list/', list_medicines, name='list'),
    path('update/<int:pk>/', update_medicine, name='update'),
    path('delete/<int:pk>/', delete_medicine, name='delete'),
]
