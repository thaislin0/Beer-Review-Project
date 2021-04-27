from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from home.models import Cervejas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
<<<<<<< HEAD

=======
>>>>>>> 633e7c8a75c80aae3bcca17edb4837ae3bbd302c

def catalogo(request):
    cervejas = Cervejas.objects.order_by('-date_public').filter(publicada=True)
    paginator = Paginator(cervejas, 4)
    page = request.GET.get('page')
    cervejas_pagina = paginator.get_page(page)
    return render(request, 'usuarios/catalogo.html', {'cervejas': cervejas_pagina})


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('usuarios:cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('usuarios:cadastro')
        if password != password2:
            messages.error(request, 'As senhas devem ser iguais')
            return redirect('usuarios:cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usário já cadastrado')
            return redirect('usuarios:cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usário já cadastrado')
            return redirect('usuarios:cadastro')
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('usuarios:login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if campo_vazio(email) or campo_vazio(password):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('usuarios:dashboard')
            else:
                messages.error(request, 'Você ainda não criou uma conta.')
    return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        cervejas = Cervejas.objects.order_by('-date_public').filter(publicada=True)
        paginator = Paginator(cervejas, 4)
        page = request.GET.get('page')
        cervejas_pagina = paginator.get_page(page)
        id = request.user.id
        cervejas = Cervejas.objects.order_by('-date_public').filter(pessoa=id)
        return render(request, 'usuarios/dashboard.html', {'cervejas':cervejas})
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


def deleta_cerveja(request, cervejas_id):
    cervejas = get_object_or_404(Cervejas, pk=cervejas_id)
    cervejas.delete()
    return redirect('usuarios:dashboard')


def edita_cerveja(request, cervejas_id):
    cervejas = get_object_or_404(Cervejas, pk=cervejas_id)
    cervejas_a_editar = {'cervejas': cervejas}
    return render(request, 'usuarios/edita_cerveja.html', cervejas_a_editar)


def atualiza(request):
    if request.method == 'POST':
        cervejas_id = request.POST['cervejas_id']
        r = Cervejas.objects.get(pk=cervejas_id)
        r.nome_cerveja  = request.POST['nome_cerveja']
        r.origem_cerveja  = request.POST['origem_cerveja']
        r.quantidade_alcool  = request.POST['quantidade_alcool']
        r.familia_cerveja  = request.POST['familia_cerveja']
        r.descricao_cerveja  = request.POST['descricao_cerveja']
        r.tipo_cerveja  = request.POST['tipo_cerveja']
        r.nota_cerveja   = request.POST['nota_cerveja']
        if 'foto_cerveja' in request.FILES:
            r.foto_cerveja  = request.FILES['foto_cerveja']
        r.save()
        return redirect('usuarios:dashboard')


def campo_vazio(campo):
    return not campo.strip()