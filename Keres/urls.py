from django.contrib import admin
from django.urls import path, include
from core.views import *
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('course/', course, name='course'),
    path('apply/', apply, name='apply'),
    path('faq/', faq, name='faq'),
    path('admission/', admission, name='admission'),
    path('careers/', careers, name='careers'),
    path('terms/', terms, name='terms'),
    path('policy/', policy, name='policy'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    #path('', include('core.urls')),
    path('', include('blog.urls')),
    #path('', include('student.urls')),
]


