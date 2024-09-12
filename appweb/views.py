from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import User
from appweb.forms import SpeakerForm, UserRegistrationForm


# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, 'index.html', {"users": users})


def form(request):
    data = {"form": SpeakerForm()}
    return render(request, 'form.html', data)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Captura o email e a senha do formulário
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Cria o novo usuário e faz o hash da senha
            user = User.objects.create(
                email=email,
                password=make_password(password)  # Criptografa a senha
            )
            user.save()

            return redirect('home')  # Redireciona após o registro
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})