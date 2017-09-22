from django.shortcuts import render, redirect, render_to_response
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext,loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import db_sala, db_participante, db_escrita
from .forms import SalaForm, EscritaForm
from random import randint
from datetime import datetime

@login_required
def salas(request):
    salas = db_sala.objects.all()
    return render(request, 'salas/salas_lista.html', {'title':'Lista de Salas','salas': salas})

@login_required
def sala_criar(request):

    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            sala = form.save(commit=False)
            sala.usuario = request.user
            sala.save()

            return redirect('salas')
    else:
        form = SalaForm()
    return render (request, 'salas/sala_editar.html', {'form':form})

def teste_escrita(request):
        if request.method == "POST":
            form = EscritaForm(request.POST)
            if form.is_valid():
                escrita = form.save(commit=False)
                escrita.usuario = request.user
                escrita.save()

                return redirect('escrever')
        else:
            form = EscritaForm()
        return render (request, 'salas/escrever.html', {'form':form})

@login_required
def home(request):
    assert isinstance(request, HttpRequest)
  #  participantes = db_participante.objects.all().order_by('posicao')
    paragrafos = db_escrita.objects.all().filter(sala=(db_sala.objects.all().get(pk=1)))
    return render(request, 'salas/index.html',{'title':'Bem-Vindo', 
                                                'year':datetime.now().year, 
                                                'paragrafos':paragrafos,
                                              #  'participantes': participantes
                                               })

@login_required
def tornar_participante(request):
    posicao = randint(0,9)
    participante = db_participante.objects.create(usuario=request.user, posicao_rodada = randint(0,9))
    return participante


def participar_sala(request,pk):

    p = tornar_participante()
    sala=get_object_or_404(db_sala, pk=pk)
    sala.participantes.add(p)
''' 
    return redirect(request, 'salas/index.html',{'title':'Bem-Vindo', 'year':datetime.now().year})

def handler400(request):
    #response = render_to_response('404.html', {},
     #                             context_instance=RequestContext(request))
    #response.status_code = 404
    #return response
    return render_to_response('../templates/error/400.html', {'exception': ex},
                                      context_instance=RequestContext(request), status=400)

def handler403(request):
        return render_to_response('../templates/error/403.html', {'exception': ex},
                                      context_instance=RequestContext(request), status=403)

def handler404(request):
        return render_to_response('../templates/error/404.html', {'exception': ex},
                                      context_instance=RequestContext(request), status=404)

def server_error(request):
        return render_to_response('../templates/error/500.html', {},
                                      context_instance=RequestContext(request), status=500)
 '''