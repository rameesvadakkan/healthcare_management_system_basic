from django.shortcuts import render
from . models import Bill
from . forms import BillForm
from django.shortcuts import get_object_or_404, redirect
from appointments.models import Appointment

def bill_create(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save()
            bill.total_amount = bill.consultation_fee + bill.medicine_fee + bill.laboratory_fee
            bill.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'billing/create.html', {'form': form})     

def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'billing/list.html', {'bills': bills})

def bill_mark_paid(request, pk):
    bill = get_object_or_404(Bill, pk=pk)

    # Mark bill as paid
    bill.status = 'Paid'
    bill.save()

    # 🔥 AUTO COMPLETE APPOINTMENT
    appointment = bill.appointment
    appointment.status = 'Completed'
    appointment.save()

    return redirect('appointment_list')  

from .models import Bill

def bill_detail(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    return render(request, 'billing/detail.html', {'bill': bill})

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def bill_pdf(request, pk):
    bill = get_object_or_404(Bill, pk=pk)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{bill.id}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    y = height - 50
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Hospital Invoice")

    p.setFont("Helvetica", 12)
    y -= 40
    p.drawString(50, y, f"Patient: {bill.appointment.patient.name}")
    y -= 20
    p.drawString(50, y, f"Doctor: {bill.appointment.doctor.name}")
    y -= 20
    p.drawString(50, y, f"Date: {bill.appointment.date}")

    y -= 30
    p.drawString(50, y, f"Consultation Fee: ₹ {bill.consultation_fee}")
    y -= 20
    p.drawString(50, y, f"Medicine Fee: ₹ {bill.medicine_fee}")
    y -= 20
    p.drawString(50, y, f"Laboratory Fee: ₹ {bill.laboratory_fee}")

    y -= 30
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, f"Total Amount: ₹ {bill.total_amount}")

    y -= 30
    p.setFont("Helvetica", 12)
    p.drawString(50, y, f"Status: {bill.status}")

    p.showPage()
    p.save()
    return response

def bill_payment(request, pk):
    bill = get_object_or_404(Bill, pk=pk)

    if bill.status == 'Paid':
        return redirect('bill_detail', pk=bill.id)

    if request.method == 'POST':
        payment_mode = request.POST.get('payment_mode')

        bill.status = 'Paid'
        bill.payment_mode = payment_mode
        bill.save()

        # Mark appointment completed
        appointment = bill.appointment
        appointment.status = 'Completed'
        appointment.save()

        return redirect('bill_detail', pk=bill.id)

    return render(request, 'billing/payment.html', {'bill': bill})