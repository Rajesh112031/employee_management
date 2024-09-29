from django.db import models
from django.utils import timezone

class Login(models.Model):
    user_name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.user_name

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('HR', 'HR'),
        ('Manager', 'Manager'),
        ('Sales', 'Sales'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    COURSE_CHOICES = [
        ('MCA', 'MCA'),
        ('BCA', 'BCA'),
        ('BSC', 'BSC'),
    ]

    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    course = models.CharField(max_length=3, choices=COURSE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Format the created_at date as DD/MM/YYYY
        date_formatted = self.created_at.strftime('%d/%m/%Y')
        return f"{self.name} - {date_formatted}"
