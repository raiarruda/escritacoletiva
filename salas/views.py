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
def home(request):
    salas = db_sala.objects.all()
    return render(request, 'salas/salas_lista.html', {'title':'Lista de Salas','salas': salas})


@login_required
def sala(request,pk):
    assert isinstance(request, HttpRequest)
    p = db_participante.objects.create(usuario=request.user, posicao_rodada = randint(0,9))

    participa_sala = db_sala.objects.all().get(pk=pk).participantes.add(p)
    participantes = db_sala.objects.all().get(pk=pk).participantes.all().order_by('posicao_rodada')
    #participantes = db_participante.objects.all().order_by('posicao_rodada')
    paragrafos = db_escrita.objects.all().filter(sala=(db_sala.objects.all().get(pk=pk)))
    sala = db_sala.objects.all().get(pk=pk)
    return render(request, 'salas/index.html',{'title':'Bem-Vindo', 
                                                'year':datetime.now().year, 
                                                'paragrafos':paragrafos,
                                                'sala': sala,
                                                'participantes':participantes
                                               })

@login_required
def sala_nova(request):

    if request.method == "POST":

        form = SalaForm(request.POST)
        if form.is_valid():
            sala = form.save(commit=False)
            sala.usuario = request.user
            sala.save()

            return redirect('salas')
        else:
           #para o botao cancela
            return redirect('salas') 
    else:
        form = SalaForm()
    return render (request, 'salas/sala_nova.html', {'form':form})


def teste_escrita(request):
        if request.method == "POST":
            form = EscritaForm(request.POST)
            if form.is_valid():
                escrita = form.save(commit=False)
                escrita.usuario = request.user
            #    escrita.sala = 
                escrita.save()

                return redirect('escrever')
            else:
                #para o botao cancela
                return redirect('escrever')
        else:
            form = EscritaForm()
        return render (request, 'salas/escrever.html', {'form':form})
