# Planejamento da Arquitetura de Software: FamilyFinance.AI

Este documento apresenta as decisões e especificações arquiteturais para a implementação do **FamilyFinance.AI**, utilizando o ecossistema moderno do Next.js 16 (com suporte a React 19) e integração com Inteligência Artificial.

---

## 🏗️ 1. Arquitetura Geral da Aplicação

A aplicação adota um padrão híbrido baseado no Next.js (App Router), dividindo responsabilidades entre o servidor e o cliente para maximizar a performance e segurança:

*   **React Server Components (RSC):** Utilizados por padrão para a renderização de telas inteiras, consultas diretas ao banco de dados PostgreSQL via Prisma ORM e proteção de rotas no servidor. Reduzem drasticamente a quantidade de Javascript enviado ao navegador.
*   **React Client Components (RCC):** Utilizados estritamente para elementos interativos que necessitam de gerenciamento de estado local ou eventos de usuário (formulários, gráficos interativos, modais). São demarcados com a diretiva `"use client"` no topo do arquivo.
*   **Server Actions:** Utilizadas para operações de mutação de dados (criação de transações, exclusão de categorias, envio de convites familiares), substituindo a necessidade de expor rotas de API tradicionais para formulários internos.
*   **Route Handlers:** Utilizados para endpoints de integração externa ou quando processamentos assíncronos prolongados demandam fluxos independentes de streaming.

---

## 🗄️ 2. Modelo Físico do Banco de Dados (Prisma Schema)

O banco de dados PostgreSQL será modelado utilizando o Prisma ORM. Abaixo está a representação conceitual e a declaração exata do arquivo `schema.prisma` a ser implementado pelo Aluno A:

```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

enum Role {
  OWNER
  MEMBER
}

model User {
  id           String        @id @default(uuid())
  name         String
  email        String        @unique
  passwordHash String
  role         Role          @default(MEMBER)
  familyId     String?       // Chave estrangeira para o Grupo Familiar
  family       Family?       @relation(fields: [familyId], references: [id], onDelete: SetNull)
  transactions Transaction[]
  createdAt    DateTime      @default(now())
  updatedAt    DateTime      @updatedAt
}

model Family {
  id           String        @id @default(uuid())
  name         String
  createdAt    DateTime      @default(now())
  updatedAt    DateTime      @updatedAt
  members      User[]
  categories   Category[]
  transactions Transaction[]
  aiPredictions AIPrediction[]
}

model Category {
  id           String        @id @default(uuid())
  name         String
  color        String        @default("#cbd5e1") // Hex da cor visual no dashboard
  familyId     String?       // Nullable: categorias globais da aplicacao vs customizadas da familia
  family       Family?       @relation(fields: [familyId], references: [id], onDelete: Cascade)
  transactions Transaction[]
  createdAt    DateTime      @default(now())
  
  @@unique([name, familyId])
}

model Transaction {
  id          String   @id @default(uuid())
  amount      Float    // Valores negativos representam despesas; positivos receitas
  description String
  date        DateTime @default(now())
  categoryId  String
  category    Category @relation(fields: [categoryId], references: [id])
  userId      String
  user        User     @relation(fields: [userId], references: [id])
  familyId    String   // Chave para isolamento rapido (Multi-tenant)
  family      Family   @relation(fields: [familyId], references: [id], onDelete: Cascade)
  createdAt   DateTime @default(now())
}

model AIPrediction {
  id          String   @id @default(uuid())
  month       Int
  year        Int
  suggestions String   // Armazena as recomendacoes formatadas em Markdown
  familyId    String
  family      Family   @relation(fields: [familyId], references: [id], onDelete: Cascade)
  createdAt   DateTime @default(now())
  
  @@unique([month, year, familyId])
}
```

---

## 🔒 3. Isolamento Multi-tenant e Proteção de Dados

Para garantir que dados financeiros de um grupo familiar não sejam expostos a outros inquilinos (*tenants*):

1.  **Chave de Tenancy Rígida (`familyId`):** Quase todas as entidades críticas (`Transaction`, `Category`, `AIPrediction`) possuem um vínculo direto com a tabela `Family`.
2.  **Filtragem no Servidor:** Qualquer consulta de leitura (`findMany`, `findFirst`) executada no Prisma obrigatoriamente deve incluir a cláusula `where: { familyId: user.familyId }`. A busca é baseada no `familyId` contido na sessão JWT do usuário autenticado no servidor, evitando que parâmetros de requisição maliciosos no cliente manipulem os dados.
3.  **Mutações Seguras:** Nas Server Actions de escrita, o `familyId` do registro a ser criado ou atualizado é injetado diretamente da sessão autenticada.

---

## 🤖 4. Integração com Inteligência Artificial (Google Gemini)

O módulo de planejamento de gastos utilizará a API do Google Gemini (modelo `gemini-1.5-flash`) de forma assíncrona.

```
+-------------------+           +---------------------+           +------------------------+
|   Componente UI   | --------> |    Route Handler    | --------> |      API do Gemini     |
|   Dashboard IA    |           |   (Servidor Next)   |           |    (Google Cloud)      |
| (RCC com Loader)  | <======== | (Filtra & Anonimiza)| <======== | (Retorna Sugestoes JSON)|
+-------------------+           +---------------------+           +------------------------+
```

### Prompt de Sistema (System Prompt) Proposto
```text
Voce eh o assistente virtual financeiro do FamilyFinance.AI. Sua tarefa eh analisar a lista de gastos da familia fornecida em formato JSON e propor metas de economia para o proximo mes.
Regras estritas:
1. Classifique o nivel de saude financeira do grupo familiar em: EXCELENTE, ATENCAO ou CRITICO.
2. Aponte as 3 categorias onde a familia mais gastou dinheiro.
3. Defina metas numericas de reducao de gastos para essas 3 categorias principais.
4. Responda em Portugues do Brasil usando estritamente a formatacao JSON com chaves: "status", "topDespesas", "metas" e "dicas".
```

---

## 📂 5. Estrutura de Diretórios Sugerida para o Projeto Next.js 16

```text
familyfinance-ai/
├── src/
│   ├── app/                    # App Router (Next.js 16)
│   │   ├── (auth)/             # Grupo de rotas de login e cadastro
│   │   │   ├── login/page.tsx
│   │   │   └── register/page.tsx
│   │   ├── dashboard/          # Area interna da aplicacao
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx        # Dashboard Principal
│   │   │   ├── transactions/   # CRUD de Transações
│   │   │   └── ai-planner/     # Planejamento com IA
│   │   ├── api/                # Route Handlers para integracoes
│   │   │   ├── auth/[...nextauth]/route.ts
│   │   │   └── ai/route.ts
│   │   ├── layout.tsx
│   │   └── page.tsx            # Landing Page publica
│   ├── components/             # Componentes reutilizaveis UI/UX
│   │   ├── ui/                 # Componentes atomicos do Shadcn
│   │   ├── transactions-form.tsx
│   │   ├── chart-bar-expenses.tsx
│   │   └── sidebar.tsx
│   ├── lib/                    # Utilitarios e configuracoes
│   │   ├── prisma.ts           # Instancia singleton do Prisma Client
│   │   ├── gemini.ts           # Inicializacao do SDK da Google AI
│   │   └── utils.ts
│   ├── actions/                # Server Actions para mutacoes
│   │   ├── transactions.ts
│   │   └── family.ts
├── prisma/
│   ├── schema.prisma
│   └── seed.ts
├── public/
├── docker-compose.yml
├── package.json
└── tsconfig.json
```
