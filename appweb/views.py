from django.shortcuts import render, redirect
from .models import User, Estudante
from appweb.forms import EstudanteRegistrationForm
from django.db import IntegrityError


# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, 'index.html', {"users": users})


def form(request):
    data = {"form": EstudanteRegistrationForm()}
    return render(request, 'form.html', data)

def tipo_cadastro(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')

        if tipo == 'estudante':
            return redirect('cadastrar_estudante')  # Redireciona para a página de cadastro de estudante
        elif tipo == 'professor':
            return redirect('cadastrar_professor')  # Redireciona para a página de cadastro de professor

    return render(request, 'tipo_cadastro.html')  # Exibe o template se não for POST


def cadastrar_estudante(request):
    if request.method == 'POST':
        form = EstudanteRegistrationForm(request.POST)
        if form.is_valid():
            # Captura os dados do formulário
            nome = form.cleaned_data['nome']
            email_institucional = form.cleaned_data['email_institucional']
            curso = form.cleaned_data['curso']
            periodo = form.cleaned_data['periodo']
            matricula = form.cleaned_data['matricula']
            senha = form.cleaned_data['senha']  # Captura a senha do formulário

            try:
                # Verifica se o email já existe
                if User.objects.filter(email=email_institucional).exists():
                    form.add_error('email_institucional', 'Este email já está em uso.')
                else:
                    # Cria o novo usuário usando o UserManager
                    user = User.objects.create_user(
                        email=email_institucional,
                        password=senha  # O UserManager já criptografa a senha
                    )

                    # Cria a instância do estudante associada ao usuário
                    estudante = Estudante(
                        user=user,
                        nome=nome,
                        email_institucional=email_institucional,
                        curso=curso,
                        periodo=periodo,
                        matricula=matricula
                    )
                    estudante.save()  # Agora salva o estudante no banco de dados

                    return redirect('home')  # Redireciona para a página inicial ou outra página
            except IntegrityError:
                form.add_error(None, "Erro ao criar o usuário. Por favor, tente novamente.")
    else:
        form = EstudanteRegistrationForm()

    return render(request, 'cadastrar_estudante.html', {'form': form})
