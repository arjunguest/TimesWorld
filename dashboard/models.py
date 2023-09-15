from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager

from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

ROLE_CHOICES = (
    ("student", "Student"),
    ("staff", "Staff"),
    ("editor", "Editor"),
    ("admin", "Admin"),
)

class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password=None, role=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.role = "admin"
        user.is_staff = True
        user.save(using=self._db)
        return user

class Customer(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length = 20, choices = ROLE_CHOICES, default = 'student')
    country = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    mobile = PhoneNumberField(null=True, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomerUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin