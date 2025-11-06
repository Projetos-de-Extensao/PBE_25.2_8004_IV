from rest_framework import viewsets
from .models import Aluno, Professor, Coordenador, Disciplina, Vaga, Candidatura, AtividadeMonitoria
from .serializers import AlunoSerializer, ProfessorSerializer, CoordenadorSerializer, DisciplinaSerializer, VagaSerializer, CandidaturaSerializer, AtividadeMonitoriaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CoordenadorViewSet(viewsets.ModelViewSet):
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class VagaViewSet(viewsets.ModelViewSet):
    serializer_class = VagaSerializer

    def get_queryset(self):
        queryset = Vaga.objects.all()

        status_vaga_param = self.request.query_params.get('status')
        status_choices = [choice[0] for choice in Vaga.StatusVaga.choices]

        if status_vaga_param and status_vaga_param.upper() in status_choices:
            queryset = queryset.filter(status=status_vaga_param.upper())

        titulo_param = self.request.query_params.get('titulo')
        if titulo_param:
            queryset = queryset.filter(titulo__icontains=titulo_param)

        descricao_param = self.request.query_params.get('descricao')
        if descricao_param:
            queryset = queryset.filter(descricao__icontains=descricao_param)

        return queryset

class CandidaturaViewSet(viewsets.ModelViewSet):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer

class AtividadeMonitoriaViewSet(viewsets.ModelViewSet):
    queryset = AtividadeMonitoria.objects.all()
    serializer_class = AtividadeMonitoriaSerializer