from django.conf.urls import include, url

from datetime import datetime

import django.contrib.auth.views
from . import forms
from . import views


urlpatterns = [
    #url(r'^$', views.login, name=login),  
    url(r'^home', views.home, name='home'),
    url(r'^sala/(?P<pk>[0-9]+)/$', views.sala, name='sala'),
    url(r'^salas/nova/$', views.sala_nova, name='sala_nova'),
    url(r'^escrever/$', views.teste_escrita, name='escrever'),  
  #  url(r'^salas/participar/(?P<pk>[0-9]+)/$',views.participar_sala, name = 'participar_sala'),
    url(r'^$',
        django.contrib.auth.views.login,
        {
            'template_name': 'salas/login.html',
            'authentication_form': forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Entrar',
                'year': datetime.now().year,
            },
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
#    url(r'^chat', views.chat, name='chat'),
#    url(r'^temas', app.views.temas, name='temas'),
#    url(r'^titulo', app.views.titulo, name='titulo'),
#    url(r'^aguardo', app.views.aguardo, name='aguardo'),
#    url(r'^escrita', app.views.escrita, name='escrita'),
]
