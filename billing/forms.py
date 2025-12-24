from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['consultation_fee', 'medicine_fee', 'laboratory_fee', 'total_amount', 'status']