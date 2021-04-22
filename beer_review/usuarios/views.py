from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('usuarios:cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('usuarios:cadastro')
        if password != password2:
            print('As senhas devem ser iguais')
            return redirect('usuarios:cadastro')
        if User.objects.filter(email=email).exists():
            print('Usário já cadastrado')
            return redirect('usuarios:cadastro')
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect('usuarios:login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def dashboard(request):
    pass


def logout(request):
    pass
