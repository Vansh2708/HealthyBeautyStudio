
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
        # Manually get data from form fields
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time') 
        service = request.POST.get('service')

        # Save to database
        Appointment.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            service=service
        )
         # Email to customer
        customer_subject = 'Appointment Confirmation - Healthy Beauty Studio'
        customer_message = f"""
        Hi {name},

        ✅ Your appointment is confirmed!
  
        📅 Date: {date}
        🕒 Time: {time}
        💇‍♀️ Service: {service}

        We look forward to seeing you!

      Healthy Beauty Studio
        """

        send_mail(
            customer_subject,
            customer_message,
            'rjain84291@gmail.com',  # sender (must match EMAIL_HOST_USER)
            [email],                # recipient (customer)
            fail_silently=False,
        )

        # Email to studio owner
        owner_subject = f'New Appointment Booked by {name}'
        owner_message = f"""
A new appointment has been booked:

👤 Name: {name}
📧 Email: {email}
📞 Phone: {phone}
💇‍♀️ Service: {service}
📅 Date: {date}
🕒 Time: {time}
        """

        send_mail(
            owner_subject,
            owner_message,
            'rjain84291@gmail.com',
            ['rjain84291@gmail.com'],  # Replace with actual owner email
            fail_silently=False,
        )

        messages.success(request, 'Appointment booked! Confirmation sent to your email.')

        # Send success message
        #messages.success(request, 'Your Appointment is booked!')

        # Redirect to home
        return redirect('home')

   return render(request, 'appointment.html')