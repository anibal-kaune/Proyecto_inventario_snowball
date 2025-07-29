from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'apellido', 'email', 'telefono', 'password1', 'password2', 'is_staff', 'is_superuser']

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'apellido', 'email', 'telefono', 'is_active', 'is_staff', 'is_superuser']