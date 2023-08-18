'''from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_lenght=50)
    last_name = forms.CharField(max_lenght=50)
    class meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')'''