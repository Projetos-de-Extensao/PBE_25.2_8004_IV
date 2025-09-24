# Documento de Visão – Sistema Acadêmico: Programa TA e Monitoria

## Introdução
Este documento descreve a visão geral do sistema acadêmico de gerenciamento do Programa de TA e Monitoria. O objetivo é apresentar os problemas enfrentados, os objetivos do projeto, os requisitos e os principais atores envolvidos.

## Descrição do Problema
O gerenciamento atual do processo de monitoria é manual, pouco padronizado e suscetível a falhas. Isso gera:
- Retrabalho administrativo.
- Atraso em entrevistas e aprovações.
- Comunicação falha entre candidatos, professores e organizadores.

## Objetivos
- Automatizar inscrição, seleção e acompanhamento dos candidatos.
- Facilitar a comunicação entre todos os atores do processo.
- Garantir transparência e rastreabilidade de cada etapa.
- Disponibilizar relatórios gerenciais para suporte à decisão.

## Atores
- **Candidato (Aluno)** – realiza inscrição, acompanha status e assina termo de participação.
- **Professor** – define disponibilidade, entrevista, aprova/reprova e acompanha desempenho.
- **Organizador (CASA)** – coordena entrevistas, relatórios e acompanhamento.
- **Sistema** – valida critérios automaticamente e envia notificações.

## Requisitos Funcionais
1. Permitir inscrição de candidatos no programa.
2. Validar critérios de elegibilidade (CR geral ≥ 7, CR disciplina ≥ 8, matrícula ativa e ≥ 800h).
3. Agendar entrevistas entre candidatos e professores.
4. Enviar notificações (inelegibilidade, entrevistas, aprovações/reprovações).
5. Registrar assinatura de termo de participação.
6. Acompanhar desempenho dos alunos aprovados.
7. Gerar relatórios de acompanhamento.

## Requisitos Não Funcionais
- Implementação em Django.
- Banco de dados relacional.
- Autenticação e autorização por perfil.
- Escalabilidade para múltiplas unidades.
- Interface simples e intuitiva.
- Integração com e-mail e WhatsApp.

## Regras de Negócio
- Apenas professores podem aprovar candidatos.
- Apenas CASA pode agendar entrevistas.
- Apenas CASA e professores podem enviar notificações.
- Apenas CASA e professores podem acompanhar desempenho.

## Conclusão
Este documento de visão estabelece a base conceitual do sistema, permitindo clareza na definição de metas e diretrizes de desenvolvimento.

## Referências
> Documento de Visão – Exemplo acadêmico.  
> Materiais de apoio sobre Engenharia de Requisitos.


