from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time'
            }),
        }


    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if doctor and date and time:
            exists = Appointment.objects.filter(
                doctor=doctor,
                date=date,
                time=time
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "This doctor already has an appointment at this date and time."
                )

        return cleaned_data        
        