
# import form class from django
from django import forms

# import AppModel from models.py
from .models import *


# create a ModelForm
class AppForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Application
        fields = ('full_name', 'phone_number', 'email', 'address', 'nrc', 'gender', 'desired_program')
        labels = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'email': 'Email',
            'address': 'Address',
            'nrc': 'NRC',
            'gender': 'Gender',
            'desired_program': 'Desired Program'
        }
        widgets = {
            'gender': forms.RadioSelect(),
            'desired_program': forms.Select(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['nrc'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['desired_program'].widget.attrs.update({'class': 'form-control'})


# create a ModelForm
class ContactForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Contact
        fields = ('full_name', 'subject', 'email', 'message')
        labels = {
            'full_name': 'Full Name',
            'subject': 'Subject',
            'email': 'Email',
            'message': 'Message',
        }
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control'})
    