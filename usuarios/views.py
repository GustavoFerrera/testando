from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth

def cadastro(request):
    if request.method == "GET":
        return render(request, 'galeria/register.html')
    else: 
        username = request.POST.get('username')
        senha = request.POST.get('senha')

    user = User.objects.filter(username=username).first()
    
    if user:
        return HttpResponse('Já existe um usuário com esse username')

    user=User.objects.create_user(username=username, password=senha)
    user.save()

    return HttpResponse('usuario cadastrado com sucesso')

def login(request):
    if request.method =="GET":
        return render(request, 'galeria/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        
        if user:
            login_auth(request, user)
            return redirect('/home/')
        else:
            return HttpResponse('login ou senha inválido')