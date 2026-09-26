# Planejamento da Sprint 1: Divisão de Atividades e Guia de Metas

Este documento serve como guia prático para a **Sprint 1** do projeto *FamilyFinance.AI*. Ele detalha as tarefas selecionadas do Product Backlog, sua estimativa de esforço relativo e apresenta duas propostas de distribuição de tarefas para a equipe de 5 alunos: a **Divisão ADS** (nível superior, focada em engenharia e arquitetura) e a **Divisão Técnico em Informática para Internet** (nível técnico, focada em interface, roteamento e consumo de APIs).

---

## 📅 1. Visão Geral da Sprint 1
*   **Duração:** 2 semanas (10 dias úteis de desenvolvimento).
*   **Meta da Sprint:** Estabelecer a interface do usuário, o roteamento da aplicação, o fluxo de autenticação e o registro/exibição de gastos diários integrados com IA.
*   **Capacidade Estimada da Equipe:** $16$ Story Points (ADS) ou $13$ Story Points (Técnico).

---

## 🗂️ 2. TRILHA A: Divisão de Tarefas - Curso Superior em ADS
Esta trilha é voltada para a complexidade da Engenharia de Software, modelagem de banco de dados física e segurança multi-tenant.

### Quadro de Distribuição da Sprint 1 (ADS)

| Aluno | Perfil Técnico | Tarefas Designadas | Esforço (SP) |
| :--- | :--- | :--- | :---: |
| **Aluno A** | Engenheiro de Infra & Banco | **TS01:** Setup inicial do Next.js 16 (TypeScript, Tailwind, Shadcn).<br>**TS02:** Configuração do Docker Compose + PostgreSQL + Prisma ORM. | **3 SP** |
| **Aluno B** | Engenheiro de Segurança & Multi-tenant | **TS03:** Fluxo de Autenticação com Next-Auth (Auth.js) e JWT.<br>**TS04:** Criação do modelo de convites familiares e vinculação lógica via `familyId`. | **5 SP** |
| **Aluno C** | Engenheiro Frontend & UI | **TS05:** Tela e formulário mobile-first de registro de gastos diários.<br>**TS06:** Listagem interativa cronológica reversa de gastos com filtros por data. | **3 SP** |
| **Aluno D** | Engenheiro Backend & Regras de Negócio | **TS07:** Criação das APIs de categorias de despesa (CRUD).<br>**TS08:** Implementação da lógica de exclusão com reatribuição para categoria "Outros". | **2 SP** |
| **Aluno E** | Engenheiro de Integração & IA | **TS09:** Conexão inicial com a API do Gemini via Vercel AI SDK.<br>**TS10:** Lógica de processamento assíncrono das transações para inferência de orçamentos. | **3 SP** |
| **Total** | **Capacidade Alocada** | | **16 SP** |

---

## 🗂️ 3. TRILHA B: Divisão de Tarefas - Técnico em Informática para Internet (Alternativa)
Esta trilha alternativa é ajustada para o nível técnico, priorizando o desenvolvimento web frontend responsivo, roteamento de páginas, manipulação de formulários locais e consumo de APIs externas com menor sobrecarga de infraestrutura complexa.

### Quadro de Distribuição da Sprint 1 (Técnico)

| Aluno | Perfil Técnico | Tarefas Designadas | Esforço (SP) |
| :--- | :--- | :--- | :---: |
| **Aluno 1** | Web Designer & CSS Specialist | **TT01:** Prototipação e estilização responsiva do Dashboard usando Tailwind CSS.<br>**TT02:** Estilização das páginas públicas (Landing Page, Login, Cadastro). | **3 SP** |
| **Aluno 2** | Frontend Integrator (Roteamento) | **TT03:** Criação do roteamento de páginas (App Router) e navegação (Sidebar).<br>**TT04:** Roteamento protegido (proteção de páginas internas via Middleware simplificado). | **3 SP** |
| **Aluno 3** | JS & Form Specialist | **TT05:** Desenvolvimento do formulário de gastos com validações HTML5/JavaScript.<br>**TT06:** Listagem simples de gastos diários usando estados locais do React. | **2 SP** |
| **Aluno 4** | Data Visualization Developer | **TT07:** Integração de gráficos simples (Recharts/Chart.js) no Dashboard.<br>**TT08:** Filtros de visualização gráfica por mês e por categorias padrão. | **2 SP** |
| **Aluno 5** | API & AI Integrator | **TT09:** Conexão e envio de requisições JSON de gastos para o endpoint de IA.<br>**TT10:** Renderização das sugestões orçamentárias recebidas na tela. | **3 SP** |
| **Total** | **Capacidade Alocada** | | **13 SP** |

---

## 📝 4. Detalhamento Técnico das Atividades por Trilha

### Detalhamento: Trilha B (Técnico em Informática para Internet)

#### Aluno 1: Interfaces e Estilização
*   **Tarefa TT01 (2 SP):** Criar os layouts HTML e a estilização responsiva do Dashboard usando Tailwind CSS. Focar no design móvel (Mobile-First) com barra de navegação retrátil.
*   **Tarefa TT02 (1 SP):** Desenvolver o design das páginas de Login, Cadastro e Landing Page pública, garantindo a acessibilidade visual dos botões e campos de entrada.

#### Aluno 2: Roteamento e Navegação
*   **Tarefa TT03 (2 SP):** Configurar a estrutura de pastas do Next.js App Router. Implementar a navegação dinâmica entre a Landing Page, Dashboard, Transações e Planner.
*   **Tarefa TT04 (1 SP):** Implementar uma verificação de sessão local simples no Middleware do Next.js para impedir o acesso às páginas do painel administrativo por usuários não autenticados.

#### Aluno 3: JavaScript, Formulários e Transações
*   **Tarefa TT05 (1 SP):** Desenvolver o formulário de cadastro de despesas. Validar obrigatoriedade de campos e tipos de dados usando JavaScript nativo no lado do cliente para alertar o usuário.
*   **Tarefa TT06 (1 SP):** Criar uma tabela interativa simples para listar as transações cadastradas, gerenciando os dados na tela por meio de estados locais do React (`useState`).

#### Aluno 4: Gráficos e Filtros
*   **Tarefa TT07 (1 SP):** Configurar a biblioteca Recharts ou Chart.js e criar um gráfico de pizza para mostrar a divisão percentual dos gastos por categoria.
*   **Tarefa TT08 (1 SP):** Implementar botões de filtro rápido que atualizam o gráfico dinamicamente com base nas despesas de categorias predefinidas.

#### Aluno 5: Consumo de APIs e IA
*   **Tarefa TT09 (2 SP):** Escrever a função assíncrona (`fetch`) que faz a chamada HTTP POST para enviar a lista de despesas em formato JSON para a API interna e obter as sugestões do Gemini.
*   **Tarefa TT10 (1 SP):** Desenvolver o card de sugestões da IA na tela, renderizando o texto recebido de forma limpa e tratando o estado de carregamento com uma mensagem de espera animada.

---

## 🎯 5. Guia de OKRs e Gerenciamento de Objetivos dos Alunos

Para ambas as turmas (ADS ou Técnico), os alunos devem gerenciar suas tarefas individualmente:

### OKR Geral da Sprint 1:
> **Objetivo:** Entregar a versão inicial funcional da interface, navegação e registro de transações do FamilyFinance.AI até o fim da Sprint.
*   **KR1 (Resultados-Chave):** Telas de Login, Cadastro e Dashboard 100% responsivas e funcionais.
*   **KR2:** Roteamento de páginas funcionando e impedindo acessos sem autenticação.
*   **KR3:** Registro de gastos diários atualizando a interface em tempo real.

### Diário de Bordo Diário (Checklist):
Ao final do dia de laboratório, responda no seu Git Markdown de progresso:
1.  *Qual tarefa do Kanban eu trabalhei hoje?*
2.  *O código já foi enviado para teste no repositório compartilhado (Git Branch)?*
3.  *Preciso de ajuda de outro aluno para destravar alguma parte da minha tarefa?*
