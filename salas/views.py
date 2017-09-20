from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext,loader
from datetime import datetime
from .models import db_sala, db_participante
from .forms import SalaForm, EscritaForm
from django.contrib.auth.decorators import login_required
from random import randint


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
    return render(request, 'salas/index.html',{'title':'Bem-Vindo', 'year':datetime.now().year})

@login_required
def tornar_participante(request):
    posicao = randint(0,9)
    participante = db_participante.objects.create(usuario=request.user, posicao_rodada = randint(0,9))
    return participante


def participar_sala(request,pk):

    p = tornar_participante()
    sala=get_object_or_404(db_sala, pk=pk)
    sala.participantes.add(p)

    return redirect(request, 'salas/index.html',{'title':'Bem-Vindo', 'year':datetime.now().year})
