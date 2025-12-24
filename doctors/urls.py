from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.doctor_list, name='doctor_list'),
    path('add/', views.doctor_add, name='doctor_add'),
]
