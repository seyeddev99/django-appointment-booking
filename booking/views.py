from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment


def home(request):
    return HttpResponse("Appointment Booking Project is Running ")


@login_required
def create_appointment(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')

        Appointment.objects.create(
            user=request.user,
            full_name=full_name,
            phone=phone,
            date=date,
            time=time
        )
        return redirect('my_appointments')

    return render(request, 'booking/create_appointment.html')
