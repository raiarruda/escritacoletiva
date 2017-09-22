from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import db_sala,db_participante,db_escrita

class BootstrapAuthenticationForm(AuthenticationForm):

    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Usuário'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Senha'}))

class SalaForm(forms.ModelForm):

    class Meta:
        model = db_sala
        fields = ('titulo','timer','n_rodada' ,'max_participantes')

class EscritaForm(forms.ModelForm):

#    paragrafo = forms.CharField(widget=forms.Textarea(  {
#        'class': 'form-control',
#        'placeholder': 'digite o paragrafo'}  ))

    class Meta:
        model = db_escrita
        fields = ('paragrafo','posicao_paragrafo','sala')
