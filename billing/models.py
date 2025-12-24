from django.db import models
from appointments.models import Appointment

class Bill(models.Model):
    PAYMENT_MODES = [
        ('UPI', 'UPI'),
        ('Card', 'Card'),
        ('Cash', 'Cash'),
    ]

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    medicine_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    laboratory_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=[('Pending','Pending'), ('Paid','Paid')],
        default='Pending'
    )
    payment_mode = models.CharField(
        max_length=10,
        choices=PAYMENT_MODES,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    
    
