    

from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'status')

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='Doctor').exists():
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='Doctor').exists():
            return False
        return super().has_delete_permission(request, obj)
