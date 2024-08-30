from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from uuid import uuid4
from rest_framework_simplejwt.tokens import RefreshToken

from csc.models import City

class StayWiseUserManager(BaseUserManager):
    def create_user(self, email, password, identifier=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class StayWiseUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    firstName = models.CharField(max_length=255, blank=False, null=False)
    lastName = models.CharField(max_length=255, blank=False, null=False)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    profilePicture = models.URLField(max_length=255, blank=True, null=True,
                                     default="https://img.icons8.com/fluency-systems-regular/96/user--v1.png")
    city = models.ForeignKey(
        to=City, on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    phoneNumber = PhoneNumberField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    isVerified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = StayWiseUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    class Meta:
        verbose_name = 'StayWiseUser'
        db_table = 'staywise_user'