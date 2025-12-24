from django.urls import path
from .views import patient_list, patient_add

urlpatterns = [
    path('list/', patient_list, name='patient_list'),
    path('add/', patient_add, name='patient_add'),
]
