
# import the standard Django Model
# from built-in library
from django.db import models


# Add any additional fields or methods as needed

# declare a new model with a name "AppModel"
class  Application(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    address = models.CharField(max_length=200, blank=True)
    nrc = models.CharField(max_length=14, blank=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False)
    DESIRED_PROGRAM_CHOICES = (
        ('Introduction to Business Management', 'Introduction to Business Management'),
        ('Fundamentals of Accounting', 'Fundamentals of Accounting'),
        ('Marketing and Sales Management', 'Marketing and Sales Management'),
        ('Human Resource Management', 'Human Resource Management'),
        ('Entrepreneurship and Innovation', 'Entrepreneurship and Innovation'),
        ('Project Management', 'Project Management'),
        ('Financial Management', 'Financial Management'),
        ('Introduction to Information Technology', 'Introduction to Information Technology'),
        ('Website Design and Development', 'Website Design and Development'),
        ('Database Design and Management', 'Database Design and Management'),
        ('Cybersecurity and Ethical Hacking', 'Cybersecurity and Ethical Hacking'),
        ('Network Administration and Management', 'Network Administration and Management'),
        ('Artificial Intelligence and Machine Learning', 'Artificial Intelligence and Machine Learning'),
        ('Graphic Designing', 'Graphic Designing'),
        ('Digital Art and Illustration', 'Digital Art and Illustration'),
        ('Photography', 'Photography'),
        ('Film and Television Production', 'Film and Television Production'),
        ('Animation and Visual Effects', 'Animation and Visual Effects'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Electrical Engineering', 'Electrical Engineering')
     )
    desired_program = models.CharField(max_length=50, choices=DESIRED_PROGRAM_CHOICES, blank=False)

    def __str__(self):
        return self.full_name


class  Contact(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    message = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.full_name