from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

#import the form name from forms.py

#import the blog post model from blog.models


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

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
            username = form.cleaned_data['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            
            myuser = User.objects.create_User(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            
            messages.success(request, ("Registrations Successful"))
            return redirect('register')
   
    else:
        form = RegisterForm()
   
    return render(request, 'register.html', {'form': form})




'''def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            if User.objects.filter(username=email).exists():
                form.add_error('email', 'User with this email already exists.')
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.first_name = name
                user.save()

                user = authenticate(request, username=email, password=password)
                login(request, user)

                return redirect('log')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})
'''