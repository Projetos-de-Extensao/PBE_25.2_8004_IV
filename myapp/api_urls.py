from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'alunos', views.AlunoViewSet)
router.register(r'professores', views.ProfessorViewSet)
router.register(r'coordenadores', views.CoordenadorViewSet)
router.register(r'disciplinas', views.DisciplinaViewSet)
router.register(r'vagas', views.VagaViewSet)
router.register(r'candidaturas', views.CandidaturaViewSet)
router.register(r'atividades-monitoria', views.AtividadeMonitoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]