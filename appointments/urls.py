from django.urls import path
from .views import appointment_add, appointment_list, appointment_approve, appointment_cancel

urlpatterns = [
    path('add/', appointment_add, name='appointment_add'),
    path('list/', appointment_list, name='appointment_list'),
     path('approve/<int:pk>/', appointment_approve, name='appointment_approve'),
    path('cancel/<int:pk>/', appointment_cancel, name='appointment_cancel'),
]
