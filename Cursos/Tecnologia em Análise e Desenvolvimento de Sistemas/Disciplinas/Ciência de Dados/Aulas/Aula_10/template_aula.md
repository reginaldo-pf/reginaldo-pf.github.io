# Modelo Padrão de Aulas: ADS -- IFCE Campus Tauá

Este guia estabelece os requisitos e o modelo estrutural que devem ser seguidos ao criar novas aulas para o curso de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) no IFCE Campus Tauá. O objetivo é garantir a consistência metodológica entre as aulas.

---

## 💡 1. Filosofia Pedagógica e Metodologia

Toda aula criada sob este padrão deve seguir uma sequência lógica em 4 pilares:
1. **Contextualização Prática (Problema de Negócio/Saúde):** Iniciar sempre apresentando um problema do mundo real relevante.
2. **Método Teórico Clássico:** Explicar a matemática analítica tradicional ou conceitos formais que regem o fenômeno.
3. **Abordagem Computacional (Simulação):** Mostrar como a computação resolve ou valida o problema de forma intuitiva (ex: métodos de reamostragem, simulações Monte Carlo).
4. **Tomada de Decisão Visual:** Apresentar gráficos claros (histogramas, boxplots, curvas ECDF) que guiem o aluno a tomar decisões seguras baseadas nos dados.

---

## 📝 2. Estrutura do Plano de Aula (Markdown)

Qualquer plano de aula deve conter a seguinte formatação no arquivo Markdown:

*   **Título:** "Plano de Aula: [Número] - [Tema]"
*   **Módulo:** Módulo correspondente no currículo.
*   **Objetivos de Aprendizagem:** Separados em Geral e Específicos.
*   **Cronograma Recomendado:** Linha do tempo sugerida para uma aula de 90 a 120 minutos.
*   **Slides Sugeridos:** Roteiro slide-a-slide indicando:
    *   Título do Slide.
    *   Tópicos e pontos chaves.
    *   Nota do Professor (diretriz de apresentação).
    *   Elemento Visual (gráfico, tabela ou imagem sugerida).
*   **Código Prático de Apoio:** Código em Python modularizado e com comentários claros.
*   **Exercícios:** Lista de exercícios práticos de programação ou análise para os alunos.

---

## 🐍 3. Padrão do Script Python de Apoio

Para manter a consistência visual nos notebooks dos alunos, os scripts de apoio devem seguir as regras abaixo:

*   **Estilo Visual Limpo:**
    ```python
    plt.style.use('seaborn-v0_8-colorblind') # Tema acessível
    plt.rcParams.update({
        'figure.figsize': (12, 7),
        'axes.labelsize': 14,
        'axes.titlesize': 16,
        'lines.linewidth': 2.5
    })
    ```
*   **Remoção de Borda (Despine):** Usar a função `despine()` para limpar os gráficos.
*   **Otimização de Amostragem:** Usar vetores do NumPy (`np.random.choice`) para loops de reamostragem em vez de loops puramente em Pandas, otimizando a velocidade.

---

## 📄 4. Padrão Modular em LaTeX (Beamer)

Para os slides da aula, deve-se adotar uma estrutura modularizada de arquivos `.tex` gerenciados por um `main.tex`.

### Estrutura do `main.tex`:
```latex
\documentclass[10pt]{beamer}

% Tema Limpo e Profissional
\usetheme{Madrid}
\usecolortheme{whale}

% Pacotes Essenciais
\usepackage[utf8]{inputenc}
\usepackage[portuguese]{babel}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{listings}
\usepackage{xcolor}

% Configurações de Código (Python)
\lstset{
    language=Python,
    basicstyle=\ttfamily\tiny,
    keywordstyle=\color{blue},
    stringstyle=\color{red},
    commentstyle=\color{green!60!black},
    breaklines=true,
    showstringspaces=false
}

% Metadados com Prevenção de Avisos de Metadados PDF
\title[ADS - Aula X]{Título da Aula}
\subtitle{Ementa da Aula}
\author[NomeCurto]{Nome do Professor\texorpdfstring{\\ \small{Adaptação Didática}}{}}
\institute[IFCE]{Instituto Federal do Ceará -- Campus Tauá \\ Tecnologia em Análise e Desenvolvimento de Sistemas}
\date{\today}

\begin{document}
\begin{frame}\titlepage\end{frame}
\begin{frame}{Sumário da Aula}\tableofcontents\end{frame}

% Blocos Modulares de Slides
\input{secao1_introducao}
\input{secao2_teoria}
\input{secao3_pratica}
\input{secao4_casos}
\input{secao5_conclusao}

\end{document}
```

### Regras Críticas para Slides de Conteúdo (`secao*.tex`):
1. **Evitar acentos em comentários no Listings:** Não coloque acentos (`ã`, `ç`, `é`, etc.) nos comentários de código dentro do ambiente `\begin{lstlisting}`. Prefira grafias simples para evitar erros de decodificação UTF-8 no compilador LaTeX.
2. **Uso de Colunas:** Para contrastar conceitos teóricos ou incluir imagens ao lado do texto, use as caixas de colunas:
   ```latex
   \begin{columns}
       \begin{column}{0.5\textwidth}
           % Texto ou topicos
       \end{column}
       \begin{column}{0.5\textwidth}
           % Imagem ou grafico
       \end{column}
   \end{columns}
   ```
3. **Frames Fragile:** Sempre declare `\begin{frame}[fragile]` em qualquer slide que contenha blocos de código (`lstlisting` ou `verbatim`).
4. **Metadados Limpos:** Use `\texorpdfstring` se precisar de formatações complexas como quebra de linha ou fontes nos metadados de autor/título para evitar avisos do hyperref.
