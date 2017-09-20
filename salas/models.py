from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class db_participante(models.Model):

    usuario = models.ForeignKey(User)
    posicao_rodada= models.IntegerField()
    def __str__ (self):

        return self.usuario.username

class db_sala(models.Model):
    titulo = models.CharField(max_length=100)
    timer = models.IntegerField()
    n_rodada = models.IntegerField()
    max_participantes = models.IntegerField()
    participantes = models.ManyToManyField(db_participante)

    def iniciar(self):
        self.save()

    def __str__ (self):
        return self.titulo

class db_escrita(models.Model):
    posicao_paragrafo = models.AutoField(primary_key=True)
    paragrafo = models.TextField()
    usuario = models.ForeignKey(User, null=True)

    def iniciar(self):
        self.save()

    def __str__ (self):
        p = str(self.posicao_paragrafo)
        return p
