from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm
from django.contrib.auth.decorators import login_required

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})
@login_required
def doctor_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctor_add.html', {'form': form})

@login_required
def edit_doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctor_edit.html', {'form': form})
@login_required
def delete_doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})