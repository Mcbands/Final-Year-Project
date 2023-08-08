from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

#import the form name from forms.py
from .forms import *


# Create your views here.
def apply(request):
    context={}
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            nrc = form.cleaned_data['nrc']
            gender = form.cleaned_data['gender']
            desired_program = form.cleaned_data['desired_program']

            
            #myuser = User.objects.create_user(full_name, phone_number, email, address, nrc, gender, desired_program)
        
            form.save()
            messages.success(request,"New User Application Alert!!. ")
            return redirect('index')
    else:
        form = AppForm()
    return render(request, 'apply.html', {'form': form})

def contact(request):
    context={}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            
            #myuser = User.objects.create_user(full_name, phone_number, email, address, nrc, gender, desired_program)
        
            form.save()
            messages.success(request,"New Contact Alert!!. ")
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})