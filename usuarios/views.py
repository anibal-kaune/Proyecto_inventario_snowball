from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioChangeForm

#Vistas crud usuarios
#Solo el admin puede acceder al crud de usuarios
def solo_admin(user):
    return user.is_superuser

@user_passes_test(solo_admin)
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuario_list.html', {'usuarios': usuarios})

@user_passes_test(solo_admin)
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form})

@user_passes_test(solo_admin)
def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioChangeForm(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form': form})

@user_passes_test(solo_admin)
def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuarios/usuario_delete.html', {'usuario': usuario})


#Vistas login
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

