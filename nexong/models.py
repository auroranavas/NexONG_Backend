from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

ADMIN = 'ADMIN'
VOLUNTEER = 'VOLUNTEER'
EDUCATOR = 'EDUCATOR'
FAMILY = 'FAMILY'
PARTNER = 'PARTNER'

PLAN_CHOICES = [
    (ADMIN, 'Admin'),
    (VOLUNTEER, 'Voluntario'),
    (EDUCATOR, 'Educador'),
    (FAMILY, 'Familia'),
    (PARTNER, 'Socio'),
]

class User(AbstractBaseUser):

    username = models.CharField(max_length=400, unique=True)
    email = models.EmailField(unique=True)
    avatar = models.URLField(max_length=255)
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    rol = models.CharField(
        max_length=10,
        choices=PLAN_CHOICES,
        default=FAMILY,
    )
    last_login = None
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def clean(self):
        super().clean()
        if not self.numero_telefono.isdigit():
            raise ValidationError("El número de teléfono debe contener solo dígitos.")