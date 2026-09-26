# Atividade Pré-Sprint: Pesquisa e Nivelamento Tecnológico (Trilha Técnica)

**Disciplina:** Desenvolvimento Web II / Programação para Internet  
**Projeto:** FamilyFinance.AI  
**Público-Alvo:** Equipe de 5 Alunos do Curso Técnico em Informática para Internet  

---

## 🎯 Objetivo da Atividade
Antes de iniciar a codificação prática da **Sprint 1**, cada aluno deve realizar esta atividade de pesquisa e nivelamento focada nas tecnologias específicas de suas tarefas. O objetivo é compreender os conceitos teóricos essenciais, ler a documentação de suporte e trazer exemplos simples de código para a reunião de alinhamento com o professor.

---

## 🧑‍💻 Roteiros de Pesquisa Individualizados

---

### 🎨 Aluno 1: Web Designer & CSS Specialist (Interfaces e Estilização)
*   **Seu Desafio na Sprint:** Construir a interface responsiva (Mobile-First) do Dashboard e das telas públicas (Landing Page, Login e Cadastro) usando Tailwind CSS.
*   **O que você deve pesquisar e aprender:**
    1.  **Layouts com Flexbox e Grid no Tailwind:** Como estruturar a barra lateral (Sidebar) e os cards do Dashboard de modo que se organizem sozinhos em telas de celular e de computador.
    2.  **Responsividade Baseada em Breakpoints:** Como usar os prefixos de tela do Tailwind (ex: `hidden md:block` para esconder um menu no celular e mostrar no desktop).
    3.  **Acessibilidade e Semântica HTML5:** O uso correto das tags `<header>`, `<nav>`, `<main>`, `<aside>` e `<footer>` para estruturar a página principal.
*   **Documentação e Recursos de Estudo:**
    *   [Tailwind CSS Utility-First Fundamentals](https://tailwindcss.com/docs/utility-first)
    *   [Flexbox e Grid no Tailwind CSS Docs](https://tailwindcss.com/docs/flex-direction)
*   **Entregável:** Esboço em papel (Wireframe) ou arquivo HTML/CSS simples de um painel de controle contendo uma barra lateral que se esconde no celular e 3 cards de resumos financeiros no topo.

---

### 🗺️ Aluno 2: Frontend Integrator (Roteamento e Proteção de Rotas)
*   **Seu Desafio na Sprint:** Organizar as pastas do Next.js App Router, criar as conexões de páginas do menu e desenvolver um middleware simples que impeça acesso direto ao painel por quem não está logado.
*   **O que você deve pesquisar e aprender:**
    1.  **Next.js App Router Folder Structure:** Como o Next.js mapeia pastas para rotas na URL e qual a diferença entre os arquivos `layout.tsx` e `page.tsx`.
    2.  **Navegação Sem Recarregamento:** O uso do componente `<Link>` e por que não devemos usar a tag HTML `<a>` nativa para navegação interna no Next.js.
    3.  **Middlewares de Rota:** Como funciona o arquivo `middleware.ts` na raiz do Next.js para interceptar e redirecionar requisições de páginas internas para a página de `/login`.
*   **Documentação e Recursos de Estudo:**
    *   [Next.js App Router - Defining Routes](https://nextjs.org/docs/app/building-your-application/routing/defining-routes)
    *   [Next.js Middleware Guide](https://nextjs.org/docs/app/building-your-application/routing/middleware)
*   **Entregável:** Um mini-projeto Next.js contendo 3 páginas (`/`, `/dashboard` e `/login`) e um link funcional de navegação entre elas sem que o navegador sofra um recarregamento total da página.

---

### ✍️ Aluno 3: JS & Form Specialist (Formulários e Estado React)
*   **Seu Desafio na Sprint:** Criar o formulário de inclusão de despesas, validar os dados preenchidos no frontend e atualizar dinamicamente a tabela de histórico exibida na tela.
*   **O que você deve pesquisar e aprender:**
    1.  **Estado React com hook `useState`:** Como guardar uma lista de transações na memória da página e adicionar um novo item a ela dinamicamente.
    2.  **Eventos de Formulário no React:** Como capturar os dados dos inputs no evento `onSubmit` e prevenir o comportamento padrão de atualização de página (`e.preventDefault()`).
    3.  **Validação de Formulários com Zod ou React Hook Form:** Como validar se o valor é positivo, se a data foi selecionada e impedir que o usuário envie dados em branco.
*   **Documentação e Recursos de Estudo:**
    *   [React Docs - State: A Component's Memory](https://react.dev/learn/state-a-components-memory)
    *   [Zod ORM Schema Validation](https://zod.dev/)
*   **Entregável:** Um trecho de código React (ou CodeSandbox) contendo um formulário simples de dois campos (Descrição e Valor) que, ao ser enviado, adiciona o dado inserido em uma lista (Array) e renderiza na tela de forma instantânea.

---

### 📈 Aluno 4: Data Visualization Developer (Gráficos e Filtros)
*   **Seu Desafio na Sprint:** Integrar bibliotecas gráficas React para mostrar onde a família está gastando o dinheiro e programar botões de filtros que atualizam o gráfico.
*   **O que você deve pesquisar e aprender:**
    1.  **Bibliotecas Gráficas React:** Como instalar e usar componentes prontos do Recharts ou do Chart.js.
    2.  **Mapeamento de Arrays de Dados:** Como transformar e estruturar os dados vindos do formulário (ex: despesas de alimentação, transporte, moradia) na estrutura exata de dados que o gráfico espera receber (geralmente um array de objetos `[{ name: 'Alimentação', value: 150 }]`).
    3.  **Re-renderização Gráfica Dinâmica:** Como fazer com que o gráfico mude de tamanho de forma fluida dependendo da tela do usuário (`ResponsiveContainer`).
*   **Documentação e Recursos de Estudo:**
    *   [Recharts Official Guide and Examples](https://recharts.org/)
    *   [react-chartjs-2 Examples](https://react-chartjs-2.js.org/)
*   **Entregável:** Um exemplo de código HTML/JS contendo uma lista estática de gastos simulados e o código de plotagem de um gráfico simples de pizza consumindo esta lista.

---

### 🔌 Aluno 5: API & AI Integrator (Consumo de APIs e IA)
*   **Seu Desafio na Sprint:** Fazer a chamada HTTP assíncrona que envia as despesas para o backend, receber as recomendações de IA em texto e criar um card para exibição com indicador de carregamento.
*   **O que você deve pesquisar e aprender:**
    1.  **Função Assíncrona `fetch` e async/await:** Como fazer requisições POST enviando JSON no corpo (`body`) e tratar erros de rede utilizando `try/catch`.
    2.  **API Routes do Next.js:** Como declarar rotas de servidor dentro da pasta `src/app/api/.../route.ts` para receber dados da interface cliente.
    3.  **Estados de Loader e Espera (UX):** Como criar uma variável booleana `isLoading` que, enquanto a requisição à IA está em andamento, mostra um ícone de carregamento ("Carregando orçamentos da IA...") e o oculta quando a resposta chega.
*   **Documentação e Recursos de Estudo:**
    *   [MDN Web Docs - Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
    *   [Next.js Docs - Route Handlers (API Backend)](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)
*   **Entregável:** Escrever um script Javascript funcional contendo uma função assíncrona utilizando `fetch` para enviar dados fictícios a um endpoint de testes públicos (ex: JSONPlaceholder) e imprimir o resultado no `console.log`.

---

## 📝 Instruções de Entrega e Avaliação em Sala de Aula
1.  **Fase 1 (Estudo Individual):** Cada aluno deve ler a documentação indicada e rascunhar o código de seu entregável.
2.  **Fase 2 (Alinhamento em Grupo):** No início da aula de laboratório, os 5 alunos se reunirão por 20 minutos para acoplar os exemplos rascunhados e entender como o fluxo de dados se comunicará entre as tarefas.
3.  **Fase 3 (Avaliação do Professor):** O professor passará nos computadores avaliando o mini-entregável e autorizará a equipe a criar os arquivos definitivos no repositório principal da Sprint 1 do *FamilyFinance.AI*.
