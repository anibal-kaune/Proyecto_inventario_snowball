from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    contraseña = models.CharField(max_length=30)