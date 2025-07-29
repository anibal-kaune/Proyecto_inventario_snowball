from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('rut', 'nombre', 'apellido', 'email', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('rut', 'nombre', 'apellido', 'telefono', 'email', 'password')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('rut', 'nombre', 'apellido', 'telefono', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
