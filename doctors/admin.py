from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience', 'consultation_fee')
    search_fields = ('name', 'specialization')
    list_filter = ('specialization',)
    