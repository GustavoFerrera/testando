from django.urls import path 
from galeria.views import index, home, dias45, admin, afastado, contasbloqueadas, Demissoes, falhadelogin, never, nuncaacessaram, PS60dias, verdetalhes, excelhtml
from usuarios.views import login, cadastro
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('', index, name='index'),
    path ('home/', home, name='home'),
    path ('45dias/', dias45, name='dias45'),
    path ('admins/', admin, name='admin'),
    path ('afastados/', afastado, name='afastado'),
    path ('contasbloqueadas/', contasbloqueadas, name='contasbloqueadas'),
    path ('Demissões/', Demissoes, name='Demissoes'),
    path ('falhasdelogin/', falhadelogin, name='falhadelogin'),
    path ('neverespires/', never, name='never'),
    path ('nuncaacessaram/', nuncaacessaram, name='nuncaacessaram'),
    path ('PS60dias/', PS60dias, name='PS60dias'),
    path ('verdetalhes/', verdetalhes, name='verdetalhes'),
    path('login/', login, name="login"),
    path('cadastro/', cadastro, name="cadastro"),
    path('tabela/', excelhtml, name="excelhtml"),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),
]