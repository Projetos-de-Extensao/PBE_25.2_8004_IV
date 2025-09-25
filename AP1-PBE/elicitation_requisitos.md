# Elicitação de Requisitos – Sistema Acadêmico: Programa TA e Monitoria

## Introdução
Este documento consolida os requisitos funcionais, não funcionais e as regras de negócio do sistema, com base no domínio e nos fluxos fornecidos.

## Atores Principais
- **Candidato (Aluno)**
- **Professor**
- **Organizador (CASA)**
- **Sistema (automação/serviços)**

## Requisitos Funcionais (Histórias de Usuário)

Os requisitos funcionais são descritos como histórias de usuário, focando no valor entregue a cada tipo de ator do sistema.

| ID | Ator | Funcionalidade (Eu quero...) | Benefício (Para que...) |
| :--- | :--- | :--- | :--- |
| RF01 | **Aluno** | ...visualizar as vagas de monitoria/TA disponíveis, com filtros por disciplina, professor e status. | ...eu possa encontrar oportunidades relevantes. |
| RF02 | **Aluno** | ...acessar os detalhes de uma vaga específica, incluindo descrição, requisitos e pré-requisitos. | ...eu possa decidir se tenho o perfil adequado. |
| RF03 | **Aluno** | ...realizar minha candidatura online para uma vaga, submetendo meus dados e documentos. | ...eu possa participar do processo seletivo. |
| RF04 | **Aluno** | ...acompanhar o status das minhas candidaturas (Ex: "Recebida", "Em Avaliação", "Aprovada"). | ...eu seja notificado sobre o andamento do processo. |
| RF05 | **Monitor/TA** | ...registrar minhas horas de atividade e descrever as tarefas realizadas mensalmente. | ...eu possa comprovar minha dedicação e cumprir a carga horária. |
| RF06 | **Professor** | ...cadastrar novas vagas de monitoria/TA para minhas disciplinas, definindo requisitos e número de vagas. | ...eu possa encontrar suporte para meus alunos. |
| RF07 | **Professor** | ...visualizar a lista de candidatos inscritos em minhas vagas, com acesso aos seus perfis. | ...eu possa iniciar o processo de avaliação. |
| RF08 | **Professor** | ...avaliar os candidatos através de critérios pré-definidos e selecionar o monitor/TA aprovado. | ...eu possa escolher o aluno mais qualificado. |
| RF09 | **Professor** | ...visualizar e aprovar os relatórios de atividades submetidos pelos meus monitores/TAs. | ...eu possa acompanhar o trabalho e validar as horas. |
| RF10 | **Coordenador** | ...homologar a publicação de novas vagas propostas pelos professores. | ...as vagas estejam de acordo com as diretrizes do programa. |
| RF11 | **Coordenador** | ...visualizar todos os programas de monitoria/TA ativos, com seus respectivos professores e monitores. | ...eu possa ter uma visão geral e gerenciar o programa. |
| RF12 | **Coordenador** | ...homologar os resultados finais da seleção, formalizando a nomeação dos monitores/TAs. | ...o processo seletivo seja oficializado. |

---

## Requisitos Não Funcionais (RNFs)

Os requisitos não funcionais definem os critérios de qualidade e as restrições operacionais do sistema.

### Usabilidade
- [ ] **RNF01:** A interface do sistema deve ser intuitiva e responsiva, adaptando-se a diferentes tamanhos de tela (desktop, tablet, mobile).
- [ ] **RNF02:** O tempo de aprendizado para um novo usuário realizar uma tarefa comum (ex: candidatar-se a uma vaga) deve ser inferior a 5 minutos.
- [ ] **RNF03:** O sistema deve fornecer feedback claro ao usuário após ações importantes (ex: "Candidatura enviada com sucesso!").

### Segurança
- [ ] **RNF04:** O sistema deve garantir a confidencialidade e integridade dos dados dos alunos e professores.
- [ ] **RNF05:** O acesso às funcionalidades deve ser controlado por papéis (Aluno, Professor, Coordenador), garantindo que um usuário só possa ver e fazer o que lhe é permitido.
- [ ] **RNF06:** O sistema deve incluir autenticação robusta (login/senha) e proteção contra vulnerabilidades web comuns (SQL Injection, XSS).

### Desempenho
- [ ] **RNF07:** As operações de busca e filtragem de vagas devem ser concluídas em no máximo 2 segundos.
- [ ] **RNF08:** A submissão de uma candidatura deve ser processada em menos de 3 segundos.
- [ ] **RNF09:** O sistema deve suportar até 1000 usuários simultâneos durante os períodos de pico de inscrição sem degradação significativa de performance.

### Disponibilidade
- [ ] **RNF10:** O sistema deve ter uma disponibilidade mínima de 99.5% durante o período letivo.
- [ ] **RNF11:** As janelas de manutenção devem ser planejadas para horários de baixa utilização (ex: madrugadas) e comunicadas aos usuários com antecedência.

### Escalabilidade
- [ ] **RNF12:** A arquitetura do sistema deve ser modular, permitindo a adição de novos módulos ou funcionalidades no futuro com baixo impacto na estrutura existente.

### Confiabilidade
- [ ] **RNF13:** As informações críticas (candidaturas, seleções, relatórios) devem ser persistidas de forma segura e com rotinas de backup diárias para garantir a recuperação em caso de falhas.  

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
