# Documento de Casos de Uso – Sistema Acadêmico: Programa TA e Monitoria

## Padrão
**Título** | **Ator** | **Descrição** | **Pré-condição** | **Fluxo Principal** | **Fluxos Alternativos** | **Pós-condição** | **Regras de Negócio**

---

## UC01 – Inscrever aluno no programa
**Ator:** Candidato  
**Descrição:** Permite que o candidato se inscreva no programa de TA/Monitoria.  
**Pré-condição:** Matrícula ativa.  
**Fluxo Principal:**  
1. Candidato informa nome e matrícula.  
2. Candidato informa curso e período.  
3. Candidato seleciona disciplina/vaga.  
4. Candidato informa CR geral e CR da disciplina.  
5. Sistema registra a candidatura.  
**Fluxos Alternativos:**  
4a. Se CR geral < 7 ou CR da disciplina < 8 → marcar como inelegível e notificar.  
**Pós-condição:** Candidatura registrada.  
**Regras de Negócio:** RB05, RB06.

---

## UC02 – Validar elegibilidade
**Ator:** Sistema  
**Descrição:** Valida automaticamente critérios (CRs, matrícula, horas).  
**Pré-condição:** Candidatura registrada.  
**Fluxo Principal:**  
1. Sistema consulta dados acadêmicos do aluno.  
2. Sistema avalia critérios (CR geral ≥ 7; CR disc. ≥ 8; matrícula ativa; ≥ 800h).  
3. Sistema define status: Elegível/Inelegível e notifica.  
**Pós-condição:** Status de elegibilidade definido.  
**Regras de Negócio:** RB05, RB06.

---

## UC03 – Agendar entrevista
**Atores:** Organizador (CASA), Professor, Candidato  
**Descrição:** Permite ao CASA alocar entrevistas com base na disponibilidade do professor.  
**Pré-condição:** Professor e CASA cadastrados; candidato elegível.  
**Fluxo Principal:**  
1. Sistema lista candidatos elegíveis.  
2. Professor informa disponibilidade.  
3. CASA seleciona janelas e aloca candidatos.  
4. Sistema registra entrevistas.  
5. Sistema notifica candidatos e professores.  
**Fluxos Alternativos:**  
a. Sem disponibilidade → candidato permanece pendente.  
**Pós-condição:** Entrevistas alocadas e notificadas.  
**Regras de Negócio:** RB02, RB03, RB06.

---

## UC04 – Notificar
**Atores:** Sistema, CASA, Professor  
**Descrição:** Enviar notificações (inelegibilidade, entrevistas, aprovações/reprovações) por e-mail/WhatsApp.  
**Pré-condição:** Eventos disparadores (ex.: decisão, agendamento).  
**Fluxo Principal:**  
1. Ação de sistema/CASA/Professor dispara notificação.  
2. Sistema envia via integrações configuradas.  
**Pós-condição:** Destinatários informados do evento.  
**Regras de Negócio:** RB03, RB06.

---

## UC05 – Registrar assinatura do termo
**Atores:** Aluno, Sistema  
**Descrição:** Permite assinatura do termo de participação.  
**Pré-condição:** Candidato aprovado.  
**Fluxo Principal:**  
1. Sistema gera link com token.  
2. Aluno acessa o link e aceita o termo.  
3. Sistema registra aceite (hash/IP/data-hora).  
**Pós-condição:** Assinatura registrada.  
**Regras de Negócio:** RB07.

---

## UC06 – Aprovar/Reprovar candidato
**Atores:** Professor, Sistema  
**Descrição:** Registra decisão do professor sobre a candidatura.  
**Pré-condição:** Entrevista realizada (quando aplicável).  
**Fluxo Principal:**  
1. Professor avalia o candidato.  
2. Professor define status: Aprovado/Reprovado.  
3. Sistema registra decisão e notifica o candidato.  
**Pós-condição:** Candidatura com decisão final.  
**Regras de Negócio:** RB01, RB03, RB06.

---

## UC07 – Acompanhar desempenho
**Atores:** CASA, Professor  
**Descrição:** Registro e visualização de indicadores e feedbacks durante o período de monitoria.  
**Pré-condição:** Assinatura do termo; aluno alocado.  
**Fluxo Principal:**  
1. CASA/Professor registram atividades e indicadores periódicos.  
2. Sistema apresenta painéis por disciplina/unidade/período.  
**Pós-condição:** Histórico de desempenho atualizado.  
**Regras de Negócio:** RB04.

---

## UC08 – Gerar relatórios
**Atores:** CASA (e Professor com escopos limitados)  
**Descrição:** Geração de relatórios operacionais e gerenciais.  
**Pré-condição:** Dados cadastrados/atualizados.  
**Fluxo Principal:**  
1. Usuário seleciona filtros (período, disciplina, status).  
2. Sistema gera relatório e permite exportação.  
**Pós-condição:** Relatório disponível (visualização/exportação).
