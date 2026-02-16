from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_CHOICES = (
        ('farmer', 'Farmer'),
        ('expert', 'Expert'),
        ('admin', 'Admin'),
    )

    phone = models.CharField(max_length=15, unique=True)
    region = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='farmer')
    is_verified = models.BooleanField(default=False)

    email = models.EmailField(unique=True, blank=True, null=True)

    REQUIRED_FIELDS = ['phone']
