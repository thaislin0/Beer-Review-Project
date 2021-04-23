from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from home.models import Cervejas


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
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == "" or password == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, password)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('usuarios:dashboard')
    return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('usuarios:login')


def logout(request):
    auth.logout(request)
    return redirect('template/home')


def review(request):
    if request.method == 'POST':
        nome_cerveja = request.POST['nome_cerveja']
        origem_cerveja = request.POST['origem_cerveja']
        familia_cerveja = request.POST['familia_cerveja']
        tipo_cerveja = request.POST['tipo_cerveja']
        descricao_cerveja = request.POST['descricao_cerveja']
        nota_cerveja = request.POST['nota_cerveja']
        quantidade_alcool = request.POST['quantidade_alcool']
        foto_cerveja = request.FILES['foto_cerveja']
        user = get_object_or_404(User, pk=request.user.id)
        cerveja = Cervejas.objects.create(pessoa=user, nome_cerveja=nome_cerveja, origem_cerveja=origem_cerveja, familia_cerveja=familia_cerveja, tipo_cerveja=tipo_cerveja, descricao_cerveja=descricao_cerveja, nota_cerveja=nota_cerveja, foto_cerveja=foto_cerveja, quantidade_alcool=quantidade_alcool)
        cerveja.save()
        return redirect('usuarios:dashboard')
    else:
        return render(request, 'usuarios/review.html')
