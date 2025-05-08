# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # iniciar sesión automáticamente
            return redirect('catalogo')  # redirige al catálogo o inicio
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "usuarios/login.html"
    
@login_required
def redireccion_post_login(request):
    user = request.user

    if user.is_superuser:
        return redirect('/adminpanel/pedidos/')
    else:
        return redirect('/usuarios/account/')

@login_required
def ver_cuenta(request):
    return render(request, "usuarios/account.html")

def confirmar_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Sesión cerrada.")
        return redirect("catalogo")  # REGRESO
    return render(request, "usuarios/confirmar_logout.html")