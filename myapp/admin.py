from django.contrib import admin
from .models import (Aluno, Professor, Coordenador, Disciplina, Vaga, Candidatura, AtividadeMonitoria)

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Coordenador)
admin.site.register(Disciplina)
admin.site.register(Vaga)
admin.site.register(Candidatura)
admin.site.register(AtividadeMonitoria)