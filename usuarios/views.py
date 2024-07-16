from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import RegisterForm, EditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra


def login(request):
    formulario = AuthenticationForm
    
    if request.method == "POST":
       formulario = AuthenticationForm(request, data=request.POST)
       if formulario.is_valid():
           username = formulario.cleaned_data.get("username")
           password = formulario.cleaned_data.get("password")
           user = authenticate(request, username=username, password=password)
           django_login(request, user)
           DatosExtra.objects.get_or_create(user=user)
           return redirect("inicio")
    
    
    
    return render(request, "usuarios/login.html", {"formulario": formulario})

def register(request):
    
    formulario = RegisterForm()
    
    if request.method == "POST":
        formulario = RegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
            
    
    return render(request, "usuarios/register.html", {"formulario": formulario})

@login_required
def EditarPerfil(request):
    
    formulario = EditForm(initial={"avatar": request.user.datosextra.avatar}, instance=request.user)
    
    if request.method == "POST":
        formulario = EditForm(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            datosextra = request.user.datosextra
            
            datosextra.avatar = formulario.cleaned_data.get("avatar")
            datosextra.save()
            
            formulario.save()
            return redirect("EditarPerfil")
    
    return render(request, "usuarios/EditarUsuarios.html", {"formulario": formulario})

class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = "usuarios/ChangePass.html"
    success_url = reverse_lazy("inicio")
