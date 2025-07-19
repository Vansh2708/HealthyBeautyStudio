from django import forms
from .models import Contact,Appointment
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'
        