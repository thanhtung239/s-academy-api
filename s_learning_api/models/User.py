from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    
    email = models.EmailField(_('email address'), unique=True, blank=False)
    password = models.CharField(max_length=250)
    company = models.CharField(max_length=250, blank=True)
    department = models.CharField(max_length=250, blank=True)
    gen_id = models.IntegerField(unique=True, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True)
    mobile_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=250, blank=True)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    about_me = models.CharField(max_length=500, blank=True)
    remember_token = models.CharField(max_length=250, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True, auto_now_add=False)
    delete_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    