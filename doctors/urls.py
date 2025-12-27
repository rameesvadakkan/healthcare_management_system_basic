from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.doctor_list, name='doctor_list'),
    path('add/', views.doctor_add, name='doctor_add'),
    path('edit/<int:doctor_id>/', views.edit_doctor, name='doctor_edit'),
    path('delete/<int:doctor_id>/', views.delete_doctor, name='doctor_delete'),
]
