# Planejamento Didático e Backlog: FamilyFinance.AI

Este diretório contém os materiais de apoio pedagógico e artefatos de engenharia de software desenvolvidos para simular a primeira reunião de backlog do sistema **FamilyFinance.AI**, voltado ao curso de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) e Técnico em Informática para Internet do IFCE Campus Tauá.

O sistema consiste em uma plataforma de finanças pessoais e familiares integrando inteligência artificial para o planejamento mensal de gastos, desenvolvido em **Next.js 16 (React 19)**.

---

## 📂 Guia de Artefatos Disponíveis

Clique nos links abaixo para acessar cada documento técnico e didático criado para esta aula:

1.  📖 **[Plano de Aula Detalhado](file:///home/reginaldo-fernandes/infonet/requisitos-finacas-reginaldo/plano_de_aula.md):** Contém a metodologia de ensino baseada em 4 pilares (Contextualização, Teoria Clássica, Simulação Computacional e Tomada de Decisão Visual), além de roteiro de slides sugeridos e exercícios de fixação.
2.  🗂️ **[Documento de Requisitos e Product Backlog](file:///home/reginaldo-fernandes/infonet/requisitos-finacas-reginaldo/backlog_requisitos.md):** Apresenta a lista completa de Requisitos Funcionais (RF), Não-Funcionais (RNF), Regras de Negócio (RN), histórias de usuário estimadas em Story Points (Fibonacci) e o calendário de desenvolvimento do MVP.
3.  📐 **[Planejamento da Arquitetura do Sistema](file:///home/reginaldo-fernandes/infonet/requisitos-finacas-reginaldo/arquitetura_sistema.md):** Detalha a arquitetura Next.js 16/React 19 (RSC/Server Actions), a modelagem de banco de dados física com o esquema exato do Prisma ORM para PostgreSQL, a estratégia de isolamento multi-tenant familiar e o fluxo assíncrono de IA.
4.  🎯 **[Orientações e Backlog da Sprint 1](file:///home/reginaldo-fernandes/infonet/requisitos-finacas-reginaldo/sprint_1_planejamento.md):** Documento para guiar a primeira sprint da equipe de 5 alunos, dividindo as tarefas com base em perfis técnicos e carga de pontos de história (contendo as trilhas de ADS e do Técnico). Inclui também o guia prático de OKRs individuais para o gerenciamento de metas diárias.
5.  📝 **[Atividade de Pesquisa e Nivelamento Tecnológico (Trilha Técnica)](file:///home/reginaldo-fernandes/infonet/requisitos-finacas-reginaldo/atividade_pesquisa_preparacao.md):** Atividade com roteiros de estudo específicos para cada um dos 5 alunos do curso técnico para que se capacitem conceitualmente e tragam pequenos protótipos de código antes de iniciar o desenvolvimento.
6.  📊 **[Slides da Apresentação da Aula (LaTeX Beamer)](file:///home/reginaldo-fernandes/infonet/requisitos-finacas-reginaldo/slides_aula.tex):** Código fonte LaTeX completo e compilável para a geração dos slides de apresentação em sala de aula de acordo com os padrões da ementa institucional.
7.  🐍 **[Script de Simulação de Sprints (Monte Carlo)](file:///home/reginaldo-fernandes/infonet/requisitos-finacas-reginaldo/simulador_sprint.py):** Código Python de suporte para simular a flutuação da velocidade da equipe ao longo de $10.000$ iterações, gerando a curva ECDF para tomada de decisão baseada em riscos estatísticos.

---

## 🚀 Como Executar o Script de Simulação

Para rodar a simulação estatística de Monte Carlo de velocidade da equipe, certifique-se de ter o Python 3 instalado com os pacotes `numpy` e `matplotlib`:

```bash
pip install numpy matplotlib
python simulador_sprint.py
```

Isso gerará o arquivo de imagem `ecdf_simulacao_prazo.png` contendo o gráfico de Função de Distribuição Acumulada Empírica para análise do cronograma.