from django.contrib import admin
from .models import db_sala
from .models import db_escrita
from .models import db_participante
from .forms import EscritaForm

admin.site.register(db_sala)
admin.site.register(db_escrita)
admin.site.register(db_participante)

class Escrita_Admin(admin.ModelAdmin):
    form = EscritaForm
