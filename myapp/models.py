from django.db import models
import uuid

class Pessoa(models.Model):
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=50, unique=True)
    
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nome} ({self.matricula})"

class Aluno(Pessoa):
    
    curso = models.CharField(max_length=50)
    periodo = models.IntegerField()
    cra = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

class Professor(Pessoa):
    
    departamento = models.CharField(max_length=50)
    siape = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        
class Coordenador(Pessoa):
    area_responsavel = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

class Disciplina(models.Model):
    
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Vaga(models.Model):
    
    class StatusVaga(models.TextChoices):
        RASCUNHO = 'RASCUNHO', 'Rascunho'
        PENDENTE_APROVACAO = 'PENDENTE', 'Pendente de Aprovação'
        ABERTA = 'ABERTA', 'Aberta'
        FECHADA = 'FECHADA', 'Fechada'
        CONCLUIDA = 'CONCLUIDA', 'Concluída'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    requisitos = models.TextField()
    num_vagas = models.IntegerField(default=1)
    data_abertura = models.DateField()
    data_encerramento = models.DateField()
    status = models.CharField(max_length=20, choices=StatusVaga.choices, default=StatusVaga.RASCUNHO)

    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name='vagas')
    professor_publicador = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='vagas_publicadas')
    coordenador_homologador = models.ForeignKey(Coordenador, on_delete=models.SET_NULL, null=True, blank=True, related_name='vagas_homologadas')

    def __str__(self):
        return f"{self.titulo} ({self.disciplina.codigo})"

    class Meta:
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"

class Candidatura(models.Model):
    
    class StatusCandidatura(models.TextChoices):
        SUBMETIDA = 'SUBMETIDA', 'Submetida'
        EM_AVALIACAO = 'EM_AVALIACAO', 'Em Avaliação'
        APROVADA = 'APROVADA', 'Aprovada'
        REPROVADA = 'REPROVADA', 'Reprovada'
        DESISTENTE = 'DESISTENTE', 'Desistente'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_candidatura = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=StatusCandidatura.choices, default=StatusCandidatura.SUBMETIDA)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='candidaturas')
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name='candidaturas')

    def __str__(self):
        return f"Candidatura de {self.aluno.nome} para {self.vaga.titulo}"
        
    class Meta:
        verbose_name = "Candidatura"
        verbose_name_plural = "Candidaturas"
        unique_together = ('aluno', 'vaga')

class AtividadeMonitoria(models.Model):
    
    class StatusRelatorio(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        APROVADO = 'APROVADO', 'Aprovado'
        REPROVADO = 'REPROVADO', 'Reprovado'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_registro = models.DateField()
    horas_realizadas = models.PositiveIntegerField()
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=StatusRelatorio.choices, default=StatusRelatorio.PENDENTE)

    candidatura_aprovada = models.ForeignKey(Candidatura, on_delete=models.CASCADE, related_name='atividades',limit_choices_to={'status': 'APROVADA'})
    professor_revisor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='atividades_revisadas')
    
    def __str__(self):
        return f"Atividade de {self.candidatura_aprovada.aluno.nome} em {self.data_registro}"

    class Meta:
        verbose_name = "Atividade de Monitoria"
        verbose_name_plural = "Atividades de Monitoria"