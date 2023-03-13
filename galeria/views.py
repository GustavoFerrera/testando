from django.shortcuts import render
from django.http import HttpResponse
from functions.quantidade import quantidadeapi
from functions.tabelas import tabelaapi

def index(request):
    return render(request, 'galeria/login.html')

def home(request):
    return render(request, 'galeria/home.html')

def dias45(request):
    return render(request, 'galeria/45dias.html')

def admin(request):
    return render(request, 'galeria/admin.html')

def afastado(request):
    quantidade_nunca_acessaram = quantidadeapi()
    context = {
        'qnt': quantidade_nunca_acessaram
    }
    return render(request, 'galeria/afastamento.html', context=context)

def contasbloqueadas(request):
    return render(request, 'galeria/contasbloqueadas.html')

def Demissoes(request):
    return render(request, 'galeria/Demissões.html')

def falhadelogin(request):
    return render(request, 'galeria/falhadelogin.html')

def never(request):
    return render(request, 'galeria/neverespires.html')

def nuncaacessaram(request):
    return render(request, 'galeria/nuncaacessaram.html')

def PS60dias(request):
    return render(request, 'galeria/PS60dias.html')

def verdetalhes(request):
    quantidade_nunca_acessaram = tabelaapi()
    context = {
        'tabela': quantidade_nunca_acessaram
    }
    return render(request, 'galeria/verdetalhes.html', context=context)

def excelhtml(request):
    return render(request, 'galeria/excelhtml.html')