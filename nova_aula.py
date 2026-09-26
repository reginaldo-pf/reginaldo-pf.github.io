#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilitário de Automação para Criação de Aulas e Disciplinas
IFCE -- Campus Tauá | Professor Reginaldo Pereira Fernandes
Padrão pedagógico baseado no cdd-aula-template
"""

import os
import sys
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CURSOS_DIR = os.path.join(BASE_DIR, "Cursos")

def listar_cursos():
    if not os.path.exists(CURSOS_DIR):
        return []
    return sorted([d for d in os.listdir(CURSOS_DIR) if os.path.isdir(os.path.join(CURSOS_DIR, d))])

def listar_disciplinas(curso):
    disc_dir = os.path.join(CURSOS_DIR, curso, "Disciplinas")
    if not os.path.exists(disc_dir):
        return []
    return sorted([d for d in os.listdir(disc_dir) if os.path.isdir(os.path.join(disc_dir, d)) and not d.startswith(".")])

def criar_disciplina(curso, disciplina):
    disc_path = os.path.join(CURSOS_DIR, curso, "Disciplinas", disciplina)
    for sub in ["Aulas", "Avaliacoes", "Referencias"]:
        os.makedirs(os.path.join(disc_path, sub), exist_ok=True)
    
    readme_path = os.path.join(disc_path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"""# {disciplina}
**Curso:** {curso}  
**Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá  
**Professor:** Reginaldo Pereira Fernandes  

---

## 🎯 Ementa e Objetivos
- Objetivos e conteúdos programáticos da disciplina.

---

## 🗂️ Estrutura da Disciplina

### 📖 [Aulas](Aulas/)
- Diretório de aulas sequenciais e roteiros práticos.

### 📝 [Avaliacoes](Avaliacoes/)
- Provas, listas e atividades avaliativas.

### 📚 [Referencias](Referencias/)
- Planos de ensino (PUD), livros e referências recomendadas.
""")
    print(f"✨ Disciplina '{disciplina}' criada com sucesso em:\n   {disc_path}")
    return disc_path

def criar_aula(curso, disciplina, aula_numero, titulo):
    disc_path = os.path.join(CURSOS_DIR, curso, "Disciplinas", disciplina)
    if not os.path.exists(disc_path):
        criar_disciplina(curso, disciplina)

    aula_dir_name = f"Aula_{aula_numero:02d}"
    base_path = os.path.join(disc_path, "Aulas", aula_dir_name)
    codigo_path = os.path.join(base_path, "codigo")
    materiais_path = os.path.join(base_path, "materiais")

    os.makedirs(codigo_path, exist_ok=True)
    os.makedirs(materiais_path, exist_ok=True)

    # 1. README.md da Aula
    readme_content = f"""# Aula {aula_numero:02d} - {titulo}
**Disciplina:** {disciplina}  
**Curso:** {curso}  
**Instituição:** Instituto Federal do Ceará (IFCE) - Campus Tauá  
**Professor:** Reginaldo Pereira Fernandes  

---

## 🎯 Objetivos de Aprendizagem
- [ ] Compreender os fundamentos conceituais e matemáticos do tópico.
- [ ] Implementar a solução computacional prática em Python.
- [ ] Analisar e interpretar os resultados visuais gerados.

---

## 📁 Estrutura de Arquivos
- `plano_de_aula.md`: Roteiro pedagógico estruturado em 4 pilares.
- `codigo/`: Scripts Python de apoio e simulações.
  - `script_apoio.py`: Código prático comentado.
- `materiais/`: Slides e apresentações em LaTeX Beamer.
  - `main.tex`: Apresentação estruturada da aula.

---

## 📚 Referências Específicas
- Documentação e referências bibliográficas do tema.
"""
    with open(os.path.join(base_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 2. plano_de_aula.md (Padrão Pedagógico IFCE Campus Tauá)
    plano_content = f"""# Plano de Aula: {aula_numero:02d} - {titulo}

* **Disciplina:** {disciplina}
* **Curso:** {curso}
* **Instituição:** Instituto Federal do Ceará (IFCE) -- Campus Tauá
* **Professor:** Reginaldo Pereira Fernandes
* **Tema:** {titulo}

---

## 💡 1. Filosofia Pedagógica e Metodologia

Esta aula segue os quatro pilares metodológicos do modelo didático:
1. **Contextualização Prática (Problema do Mundo Real):** Apresentação de um caso prático motivador.
2. **Método Teórico Clássico:** Demonstração formal dos conceitos analíticos e matemáticos passo a passo.
3. **Abordagem Computacional (Simulação):** Demonstração em código Python equivalente para validar os resultados teóricos.
4. **Tomada de Decisão Visual:** Gráficos claros para guiar a interpretação e tomada de decisão fundamentada.

---

## 🎯 2. Objetivos de Aprendizagem
- **Geral:** Capacitar os estudantes no domínio de {titulo}.
- **Específicos:**
  - Identificar os elementos teóricos e conceituais centrais.
  - Desenvolver scripts funcionais em Python para simulação e teste.
  - Interpretar e documentar as saídas obtidas.

---

## ⏱️ 3. Cronograma Recomendado (Aula de 100 minutos)
- **00 - 20 min:** Contextualização prática e desafio motivador.
- **20 - 45 min:** Formulação teórica e cálculo do exemplo passo a passo.
- **45 - 75 min:** Implementação em código Python no laboratório.
- **75 - 90 min:** Discussão dos resultados e tomada de decisão visual.
- **90 - 100 min:** Fechamento e orientações para exercícios.

---

## 💻 4. Código Prático de Apoio
Consulte o arquivo [`codigo/script_apoio.py`](codigo/script_apoio.py).

---

## 📝 5. Exercícios de Fixação
1. Exercício analítico de cálculo passo a passo.
2. Exercício prático de implementação e variação de parâmetros.
"""
    with open(os.path.join(base_path, "plano_de_aula.md"), "w", encoding="utf-8") as f:
        f.write(plano_content)

    # 3. script_apoio.py (Padrão Visual Limpo e Acessível)
    script_content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Apoio -- Aula {aula_numero:02d}: {titulo}
Disciplina: {disciplina}
IFCE Campus Tauá -- Prof. Reginaldo Pereira Fernandes
"""

import numpy as np
import matplotlib.pyplot as plt

# Configuracao visual acessivel recomendada
plt.style.use('seaborn-v0_8-colorblind')
plt.rcParams.update({{
    'figure.figsize': (10, 6),
    'axes.labelsize': 13,
    'axes.titlesize': 15,
    'lines.linewidth': 2.2
}})

def despine(ax):
    """Remove bordas superior e direita para visualizacao limpa."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

def main():
    print(f"Executando script de apoio da Aula {aula_numero:02d}: {titulo}")
    # Insira aqui os dados e simulacoes da aula

if __name__ == '__main__':
    main()
'''
    with open(os.path.join(codigo_path, "script_apoio.py"), "w", encoding="utf-8") as f:
        f.write(script_content)

    # 4. main.tex (Template Beamer Madrid/whale para IFCE Tauá)
    tex_content = f"""\\documentclass[10pt]{{beamer}}

% Tema Institucional Limpo e Profissional
\\usetheme{{Madrid}}
\\usecolortheme{{whale}}

% Pacotes Essenciais
\\usepackage[utf8]{{inputenc}}
\\usepackage[portuguese]{{babel}}
\\usepackage{{graphicx}}
\\usepackage{{booktabs}}
\\usepackage{{amsmath}}
\\usepackage{{amssymb}}
\\usepackage{{listings}}
\\usepackage{{xcolor}}

% Configuracoes de Codigo (Python)
\\lstset{{
    language=Python,
    basicstyle=\\ttfamily\\tiny,
    keywordstyle=\\color{{blue}},
    stringstyle=\\color{{red}},
    commentstyle=\\color{{green!60!black}},
    breaklines=true,
    showstringspaces=false
}}

% Metadados da Apresentacao
\\title[Aula {aula_numero:02d} - {disciplina}]{{{titulo}}}
\\subtitle{{{disciplina}}}
\\author[Prof. Reginaldo Fernandes]{{Prof. Reginaldo Pereira Fernandes}}
\\institute[IFCE]{{Instituto Federal do Cear\\'a -- Campus Tau\\'a \\\\ {curso}}}
\\date{{\\today}}

\\begin{{document}}

\\begin{{frame}}
    \\titlepage
\\end{{frame}}

\\begin{{frame}}{{Sum\\'ario da Aula}}
    \\tableofcontents
\\end{{frame}}

\\section{{Contextualiza\\c{{c}}\\~ao}}
\\begin{{frame}}{{1. Problema Pr\\'atico}}
    \\begin{{block}}{{Cen\\'ario do Mundo Real}}
        Apresenta\\c{{c}}\\~ao do problema motivador e objetivos pr\\'aticos da aula.
    \\end{{block}}
\\end{{frame}}

\\section{{M\\'etodo Te\\'orico}}
\\begin{{frame}}{{2. Fundamenta\\c{{c}}\\~ao Te\\'orica}}
    \\begin{{itemize}}
        \\item Conceitos centrais e defini\\c{{c}}\\~oes anal\\'iticas.
        \\item Exemplo matem\\'atico com n\\'umeros simplificados.
    \\end{{itemize}}
\\end{{frame}}

\\section{{Abordagem Computacional}}
\\begin{{frame}}[fragile]{{3. Implementa\\c{{c}}\\~ao em Python}}
\\begin{{lstlisting}}
# Demonstracao computacional equivalente
import numpy as np

def resolver_problema():
    pass
\\end{{lstlisting}}
\\end{{frame}}

\\section{{Conclus\\~ao}}
\\begin{{frame}}{{4. Tomada de Decis\\~ao e Conclus\\~ao}}
    \\begin{{itemize}}
        \\item Interpreta\\c{{c}}\\~ao dos resultados visuais.
        \\item Pr\\'oximos passos e exerc\\'icios.
    \\end{{itemize}}
\\end{{frame}}

\\end{{document}}
"""
    with open(os.path.join(materiais_path, "main.tex"), "w", encoding="utf-8") as f:
        f.write(tex_content)

    # 5. notebook_aula.ipynb (Jupyter Notebook)
    import json
    notebook_dict = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Aula {aula_numero:02d}: {titulo}\n",
                    f"**Disciplina:** {disciplina}  \n",
                    f"**Curso:** {curso} -- IFCE Campus Tauá  \n",
                    f"**Professor:** Reginaldo Pereira Fernandes\n",
                    "\n",
                    "---\n",
                    "## 🎯 Objetivos de Aprendizagem:\n",
                    "1. Fundamentos teóricos e analíticos do tópico.\n",
                    "2. Implementação computacional e simulação prática em Python.\n",
                    "3. Análise visual de dados e tomada de decisão fundamentada."
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "### 1. Preparação do Ambiente e Bibliotecas\n",
                    "Importação dos módulos padrão para manipulação de dados e visualização gráfica:"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 1,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "\n",
                    "plt.style.use('seaborn-v0_8-colorblind')\n",
                    "plt.rcParams.update({\n",
                    "    'figure.figsize': (10, 6),\n",
                    "    'axes.labelsize': 13,\n",
                    "    'axes.titlesize': 15,\n",
                    "    'lines.linewidth': 2.2\n",
                    "})\n",
                    "\n",
                    "print('✅ Ambiente configurado com sucesso!')"
                ]
            }
        ],
        "metadata": {
            "language_info": {"name": "python", "version": "3"},
            "kernelspec": {"name": "python3", "display_name": "Python 3"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    with open(os.path.join(codigo_path, "notebook_aula.ipynb"), "w", encoding="utf-8") as f:
        json.dump(notebook_dict, f, indent=2, ensure_ascii=False)

    # 6. index.html (Página Web Interativa da Aula)
    aula_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aula {aula_numero:02d}: {titulo} | {disciplina}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter', sans-serif; }}
    code, pre {{ font-family: 'JetBrains Mono', monospace !important; }}
    .tab-active {{
      border-color: #059669;
      color: #059669;
      background-color: rgba(5, 150, 105, 0.08);
    }}
  </style>
</head>
<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-100 min-h-screen flex flex-col">
  <header class="border-b border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 backdrop-blur sticky top-0 z-50">
    <div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
      <a href="../../index.html" class="flex items-center space-x-2 text-slate-700 dark:text-slate-300 hover:text-emerald-600 font-medium text-sm">
        <i class="fa-solid fa-arrow-left"></i>
        <span>Voltar para Disciplina</span>
      </a>
      <div class="flex items-center space-x-3">
        <a href="https://github.com/reginaldo-pf" target="_blank" class="text-slate-500 hover:text-slate-800 text-lg"><i class="fa-brands fa-github"></i></a>
      </div>
    </div>
  </header>

  <main class="flex-grow max-w-6xl mx-auto px-4 py-8 w-full">
    <div class="bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-200 dark:border-slate-700 shadow-sm mb-8">
      <span class="px-2.5 py-1 text-xs font-semibold rounded-full bg-emerald-100 text-emerald-800">Aula {aula_numero:02d}</span>
      <h1 class="text-2xl sm:text-3xl font-extrabold mt-2">{titulo}</h1>
      <p class="text-xs sm:text-sm text-slate-500 mt-1">{disciplina} • {curso} • Prof. Reginaldo Pereira Fernandes</p>

      <div class="flex flex-wrap items-center gap-3 mt-6 pt-5 border-t border-slate-100 dark:border-slate-700">
        <a href="codigo/notebook_aula.ipynb" download class="inline-flex items-center space-x-2 px-3.5 py-2 rounded-xl text-xs font-semibold bg-amber-500 text-slate-900">
          <i class="fa-solid fa-book-open"></i><span>Baixar Notebook (.ipynb)</span>
        </a>
        <a href="codigo/script_apoio.py" download class="inline-flex items-center space-x-2 px-3.5 py-2 rounded-xl text-xs font-medium bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-200">
          <i class="fa-brands fa-python text-emerald-500"></i><span>Baixar Script (.py)</span>
        </a>
      </div>
    </div>

    <div class="bg-white dark:bg-slate-800 rounded-xl p-6 border border-slate-200 dark:border-slate-700 shadow-sm">
      <h2 class="text-lg font-bold mb-4 flex items-center space-x-2">
        <i class="fa-solid fa-code text-emerald-500"></i>
        <span>Prática e Código da Aula</span>
      </h2>
      <div class="bg-slate-100 dark:bg-slate-850 px-4 py-2 border-b border-slate-200 flex items-center justify-between text-xs text-slate-500">
        <span class="font-mono font-bold text-emerald-600">In [1]:</span>
      </div>
      <pre class="p-4 text-xs overflow-x-auto"><code class="language-python"># Execução do script de apoio da Aula {aula_numero:02d}
import numpy as np

print("Ambiente configurado para: {titulo}")</code></pre>
    </div>
  </main>

  <footer class="border-t border-slate-200 py-6 text-center text-xs text-slate-500">
    <p>© 2026 IFCE Campus Tauá • Prof. Reginaldo Pereira Fernandes</p>
  </footer>
</body>
</html>
"""
    with open(os.path.join(base_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(aula_html)

    print(f"✅ Aula {aula_numero:02d} ('{titulo}') criada com sucesso!")
    print(f"   Local: {base_path}")
    print(f"   Arquivos gerados:")
    print(f"   - index.html (Página Web Interativa)")
    print(f"   - README.md")
    print(f"   - plano_de_aula.md")
    print(f"   - codigo/script_apoio.py")
    print(f"   - codigo/notebook_aula.ipynb")
    print(f"   - materiais/main.tex")

def modo_interativo():
    cursos = listar_cursos()
    if not cursos:
        print("Nenhum curso encontrado em Cursos/. Criando cursos padrao...")
        return

    print("=" * 60)
    print("🎓 Gerenciador de Aulas -- IFCE Campus Tauá")
    print("=" * 60)
    print("\nCursos disponíveis:")
    for idx, c in enumerate(cursos, 1):
        print(f"  [{idx}] {c}")

    try:
        escolha_curso = int(input(f"\nEscolha o curso (1-{len(cursos)}): ")) - 1
        if escolha_curso < 0 or escolha_curso >= len(cursos):
            print("Opção inválida.")
            return
        curso_sel = cursos[escolha_curso]
    except (ValueError, KeyboardInterrupt):
        print("\nOperação cancelada.")
        return

    disciplinas = listar_disciplinas(curso_sel)
    print(f"\nDisciplinas de '{curso_sel}':")
    for idx, d in enumerate(disciplinas, 1):
        print(f"  [{idx}] {d}")
    print(f"  [0] + Criar nova disciplina")

    try:
        escolha_disc = int(input(f"\nEscolha a disciplina (0-{len(disciplinas)}): "))
        if escolha_disc == 0:
            nova_disc = input("Nome da nova disciplina: ").strip()
            if not nova_disc:
                print("Nome inválido.")
                return
            disc_sel = nova_disc
        elif 1 <= escolha_disc <= len(disciplinas):
            disc_sel = disciplinas[escolha_disc - 1]
        else:
            print("Opção inválida.")
            return
    except (ValueError, KeyboardInterrupt):
        print("\nOperação cancelada.")
        return

    try:
        aula_num = int(input("\nNúmero da aula (ex: 2): "))
        titulo = input("Título da aula: ").strip()
        if not titulo:
            print("O título não pode ser vazio.")
            return
    except (ValueError, KeyboardInterrupt):
        print("\nOperação cancelada.")
        return

    criar_aula(curso_sel, disc_sel, aula_num, titulo)

def main():
    parser = argparse.ArgumentParser(description="Criador automático de aulas padronizadas para o IFCE Campus Tauá.")
    parser.add_argument("--curso", type=str, help="Nome completo do curso.")
    parser.add_argument("--disciplina", type=str, help="Nome da disciplina.")
    parser.add_argument("--aula", type=int, help="Número sequencial da aula.")
    parser.add_argument("--titulo", type=str, help="Título do tema da aula.")
    parser.add_argument("--nova-disciplina", action="store_true", help="Apenas criar a estrutura de uma nova disciplina.")

    args = parser.parse_args()

    if not any([args.curso, args.disciplina, args.aula, args.titulo]):
        modo_interativo()
        return

    if not args.curso or not args.disciplina:
        print("Erro: Os parâmetros --curso e --disciplina são obrigatórios no modo direto.")
        sys.exit(1)

    if args.nova_disciplina:
        criar_disciplina(args.curso, args.disciplina)
        return

    if args.aula is None or not args.titulo:
        print("Erro: É necessário informar --aula e --titulo para criar uma aula.")
        sys.exit(1)

    criar_aula(args.curso, args.disciplina, args.aula, args.titulo)

if __name__ == "__main__":
    main()
