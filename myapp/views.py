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
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class CandidaturaViewSet(viewsets.ModelViewSet):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer

class AtividadeMonitoriaViewSet(viewsets.ModelViewSet):
    queryset = AtividadeMonitoria.objects.all()
    serializer_class = AtividadeMonitoriaSerializer