from django.urls import path
from .views import bill_create, bill_list, bill_mark_paid, bill_pdf, bill_detail, bill_payment

urlpatterns = [
    path('create/', bill_create, name='bill_create'),
    path('list/', bill_list, name='bill_list'),
    path('paid/<int:pk>/', bill_mark_paid, name='bill_mark_paid'),
     path('pdf/<int:pk>/', bill_pdf, name='bill_pdf'),
     path('detail/<int:pk>/', bill_detail, name='bill_detail'),
     path('pay/<int:pk>/', bill_payment, name='bill_payment'),
]
