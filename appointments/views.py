from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from billing.models import Bill
@login_required

def appointment_add(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/add.html', {'form': form})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/list.html', {'appointments': appointments})



@login_required
def appointment_approve(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    appointment.status = 'Approved'
    appointment.save()

    # 🔥 AUTO BILL CREATE
    if not hasattr(appointment, 'bill'):
        fee = appointment.doctor.consultation_fee
        Bill.objects.create(
            appointment=appointment,
            consultation_fee=fee,
            medicine_fee=0,
            laboratory_fee=0,
            total_amount=fee
        )

    return redirect('appointment_list')

@login_required
def appointment_cancel(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'Cancelled'
    appointment.save()
    return redirect('appointment_list')