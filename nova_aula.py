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

    print(f"✅ Aula {aula_numero:02d} ('{titulo}') criada com sucesso!")
    print(f"   Local: {base_path}")
    print(f"   Arquivos gerados:")
    print(f"   - README.md")
    print(f"   - plano_de_aula.md")
    print(f"   - codigo/script_apoio.py")
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
