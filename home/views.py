
from django.shortcuts import render, redirect
from .forms import ContactForm, AppointmentForm
from django.contrib import messages
from .models import Contact,Appointment
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')  # redirect to the same page to show message
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()

            # Email to customer
            customer_subject = 'Appointment Confirmation - Healthy Beauty Studio'
            customer_message = f"""
Hi {appointment.name},

✅ Your appointment is confirmed!

📅 Date: {appointment.date}
🕒 Time: {appointment.time}
💇‍♀️ Service: {appointment.service}

We look forward to seeing you!

Healthy Beauty Studio
            """

            send_mail(
                customer_subject,
                customer_message,
                'rjain84291@gmail.com',
                [appointment.email],
                fail_silently=False,
            )

            # Email to studio owner
            owner_subject = f'New Appointment Booked by {appointment.name}'
            owner_message = f"""
A new appointment has been booked:

👤 Name: {appointment.name}
📧 Email: {appointment.email}
📞 Phone: {appointment.phone}
💇‍♀️ Service: {appointment.service}
📅 Date: {appointment.date}
🕒 Time: {appointment.time}
            """

            send_mail(
                owner_subject,
                owner_message,
                'rjain84291@gmail.com',
                ['rjain84291@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Appointment booked! Confirmation sent to your email.')
            return redirect('home')
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment.html', {'form': form})