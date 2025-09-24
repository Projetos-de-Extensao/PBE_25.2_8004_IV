# Casos de Uso – Programa TA e Monitoria

## UC01 – Inscrição
- **Ator**: Candidato  
- **Pré-condição**: Matrícula ativa  
- **Fluxo Principal**: Preenche formulário → sistema valida → registra candidatura  
- **Fluxo Alternativo**: Se não atender critérios, exibir mensagem de inelegibilidade  

## UC02 – Validação de Elegibilidade
- **Ator**: Sistema  
- **Fluxo**: Valida CR geral, CR disciplina, matrícula e horas → define status

## UC03 – Agendar Entrevista
- **Ator**: CASA, Professor  
- **Fluxo**: Professor define disponibilidade → CASA aloca candidatos → sistema notifica  

## UC04 – Aprovação/Reprovação
- **Ator**: Professor  
- **Fluxo**: Avalia candidato e define status → sistema notifica candidato  

## UC05 – Acompanhamento de Desempenho
- **Ator**: CASA, Professor  
- **Fluxo**: Inserem indicadores e feedbacks → sistema registra  

## UC06 – Relatórios
- **Ator**: CASA  
- **Fluxo**: Seleciona filtros → gera relatórios em PDF/CSV  

