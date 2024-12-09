from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
import secrets

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=350 , null=True)
    full_name = models.CharField(max_length=80 , null=True)
    phone_number = models.CharField(max_length=11, unique=True)
    password_copy = models.TextField(null=True , blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, blank=True, null=True)
    # User Manager in ./managers.py
    objects = UserManager()
    date_added = models.DateField(auto_now_add=True , null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'