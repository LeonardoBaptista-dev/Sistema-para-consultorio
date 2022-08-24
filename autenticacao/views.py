from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid
from django.shortcuts import redirect
from django.contrib.auth.models import User 
from django.contrib.messages import constants   
from django.contrib import messages


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha') 
        email = request.POST.get('email') 
        confirmar_senha = request.POST.get('confirmar_senha')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')

        try: 
            user = User.objects.create_user(username=usuario, 
                                            email=email, 
                                            password=senha, 
                                            is_active=False) 
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            return redirect('/auth/logar') 
        except: 
            messages.add_message(request, constants.ERROR, ' Erro interno do sistema')
            return redirect('/auth/cadastro')


def logar(request):
    return render(request, 'login.html')
