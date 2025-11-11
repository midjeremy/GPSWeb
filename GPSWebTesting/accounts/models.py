from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email=None, rut=None, password=None, role=None, **extra_fields):
        if not email and not rut:
            raise ValueError('El usuario debe tener un email o un RUT')
        email = self.normalize_email(email) if email else None
        user = self.model(email=email, rut=rut, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, password=password, role='supervisor', **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('tecnico', 'Técnico'),
        ('supervisor', 'Supervisor'),
    )

    email = models.EmailField(unique=True, null=True, blank=True)
    rut = models.CharField(max_length=12, unique=True, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email or self.rut
