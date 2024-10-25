from enum import Enum
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from base_user.utils import IndianMobileNumberValidator

class Role(Enum):
    ADMIN = 'ADMIN'
    OWNER = 'OWNER'
    DRIVER = 'DRIVER'
    CUSTOMER = 'CUSTOMER'

class CUserManager(UserManager):
    def create_user(self, mobile, email=None, password=None, is_staff=False,
                    is_superuser=False, **extra_fields):
        if not mobile:
            raise ValueError('Mobile number is mandatory')
        if not email:
            raise ValueError('Email is mandatory')
        if not password:
            raise ValueError('Password is mandatory')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            mobile=mobile,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)  # Save the user to the database
        return user

    def create_superuser(self, mobile, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            mobile=mobile,
            email=email,
            password=password,
            **extra_fields
        )

class BaseUser(AbstractUser):
    mobile = models.BigIntegerField(
        validators=[IndianMobileNumberValidator()],
        unique=True
    )
    username = None

    objects = CUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.get_full_name()
