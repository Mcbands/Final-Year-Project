from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

#import the form name from forms.py
from .forms import *

#import the blog post model from blog.models
from blog.models import post


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    posts = post.objects.all()
    return render(request, 'blog.html', {'posts': posts })

def contact(request):
    return render(request, 'contact.html')

def admission(request):
    return render(request, 'admission.html')

def careers(request):
    return render(request, 'careers.html')

def course(request):
    return render(request, 'course.html')

def faq(request):
    return render(request, 'faq.html')

def terms(request):
    return render(request, 'terms.html')

def policy(request):
    return render(request, 'policy.html')

'''def apply(request):
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
    return render(request, 'apply.html', context)
    '''



