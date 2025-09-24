# Elicitação de Requisitos – Sistema Acadêmico: Programa TA e Monitoria

## Introdução
Este documento consolida os requisitos funcionais, não funcionais e as regras de negócio do sistema, com base no domínio e nos fluxos fornecidos.

## Atores Principais
- **Candidato (Aluno)**
- **Professor**
- **Organizador (CASA)**
- **Sistema (automação/serviços)**

## Requisitos Funcionais (RF)
RF01. Permitir inscrição de alunos no programa (formulário com nome, matrícula, curso, período, disciplina, CR geral, CR da disciplina).  
RF02. Validar critérios de elegibilidade automaticamente (CR geral ≥ 7; CR disciplina ≥ 8; matrícula ativa; carga horária ≥ 800h).  
RF03. Cadastrar e listar vagas/disciplinas disponíveis para monitoria.  
RF04. Listar candidatos elegíveis e inelegíveis.  
RF05. Registrar disponibilidade de horário do professor para entrevistas.  
RF06. Agendar entrevistas (CASA) alocando candidatos e professores conforme disponibilidade.  
RF07. Notificar candidatos e professores (e-mail/WhatsApp): inelegibilidade, entrevista, aprovação/reprovação.  
RF08. Registrar assinatura do termo de participação (fluxo de aceite com token).  
RF09. Registrar aprovação/reprovação do candidato (apenas professor).  
RF10. Acompanhar desempenho dos alunos aprovados (indicadores e feedbacks).  
RF11. Gerar relatórios (aprovados/reprovados; presença em entrevistas; indicadores por disciplina/unidade/período).  
RF12. Exportar relatórios em CSV/PDF.  
RF13. Manter histórico das candidaturas, entrevistas e assinaturas.  
RF14. Permitir consulta de status pelo candidato (ex.: “em análise”, “elegível”, “entrevista”, “aprovado”, “reprovado”).  
RF15. Gerenciar perfis e permissões por ator (Aluno/Professor/CASA/Admin).  

## Requisitos Não Funcionais (RNF)
RNF01. Implementação em **Django**.  
RNF02. Banco de dados **relacional**.  
RNF03. **Autenticação** e **autorização** por perfil (RBAC).  
RNF04. **Segurança**: senhas com hash, HTTPS, registro de auditoria (logs).  
RNF05. **Escalabilidade** para múltiplas unidades e disciplinas.  
RNF06. **Usabilidade**: interface simples, responsiva e acessível.  
RNF07. **Integrações** com e-mail (SMTP) e WhatsApp (provedor oficial).  
RNF08. **Disponibilidade** mínima 99% no período letivo (meta).  
RNF09. **Performance**: carregamento de telas principais ≤ 2s em condições normais.  
RNF10. **LGPD**: consentimento para tratamento de dados e termo de participação.  

## Regras de Negócio (RB)
RB01. **Somente professor** pode aprovar/reprovar candidato.  
RB02. **Somente o CASA** pode agendar entrevistas.  
RB03. **Somente CASA e professor** podem enviar e-mails/WhatsApp pelo sistema.  
RB04. **Somente CASA e professor** podem registrar/acompanhar desempenho.  
RB05. Critérios de elegibilidade: **CR geral ≥ 7**, **CR disciplina ≥ 8**, **matrícula ativa**, **≥ 800 horas**.  
RB06. Notificações obrigatórias: **inelegibilidade**, **entrevista**, **aprovação/reprovação**.  
RB07. Assinatura de termo é condição para início das atividades.  

## Rastreabilidade (Requisitos ↔ Casos de Uso)
- RF01, RF02 → UC01 (Inscrever-se), UC02 (Validar elegibilidade)  
- RF05, RF06, RF07 → UC03 (Agendar entrevista), UC04 (Notificar)  
- RF08 → UC05 (Assinar termo)  
- RF09 → UC06 (Aprovar/Reprovar)  
- RF10, RF11, RF12 → UC07 (Acompanhar desempenho), UC08 (Relatórios)  
- RF15 → Transversal a todos os UC
