from django.contrib import admin
from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'total_amount', 'status')

    def has_module_permission(self, request):
        if request.user.groups.filter(name='Doctor').exists():
            return False
        return True
    