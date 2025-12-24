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

# Create your views here.
