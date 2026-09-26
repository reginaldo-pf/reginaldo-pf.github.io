# 🎓 Repositório Central de Aulas -- IFCE Campus Tauá
**Professor:** Reginaldo Pereira Fernandes  
**Organização:** `Aulas > Cursos > Disciplinas`

---

## 🏛️ Estrutura Geral dos Cursos

Este repositório centraliza o planejamento, materiais didáticos, códigos-fonte, avaliações e apresentações em LaTeX Beamer para as disciplinas ministradas no **Instituto Federal do Ceará (IFCE) - Campus Tauá**.

```text
Aulas/
├── nova_aula.py                  # Script de automação para criação rápida de aulas e disciplinas
└── Cursos/
    ├── Técnico em Informática para Internet/
    │   ├── Disciplinas/
    │   │   ├── Engenharia de Software/
    │   │   └── Análise e Projeto de Sistemas/
    │   └── Projetos/
    │       └── projeto_infonet/
    │
    ├── Técnico em Redes de Computadores/
    │   └── Disciplinas/
    │       ├── Lógica de Programação/
    │       └── Redes de Computadores/
    │
    ├── Tecnologia em Análise e Desenvolvimento de Sistemas/
    │   ├── Disciplinas/
    │   │   ├── Ciência de Dados/
    │   │   └── Banco de Dados Não-Relacionais/
    │   └── Institucional/
    │
    └── Tecnologia em Telemática/
        └── Disciplinas/
            └── _Template_Disciplina/
```

---

## 🚀 Automação: Como Criar uma Nova Aula

Para criar uma nova aula seguindo a estrutura padrão das disciplinas (`codigo/`, `materiais/`, `README.md`) e compatível com a metodologia pedagógica do IFCE, utilize o utilitário [`nova_aula.py`](file:///home/reginaldo-fernandes/Aulas/nova_aula.py):

```bash
# Modo Interativo (menu com seleção de curso e disciplina):
python3 /home/reginaldo-fernandes/Aulas/nova_aula.py

# Modo Direto (via parâmetros CLI):
python3 /home/reginaldo-fernandes/Aulas/nova_aula.py --curso "Tecnologia em Análise e Desenvolvimento de Sistemas" --disciplina "Ciência de Dados" --aula 15 --titulo "Modelos Preditivos"
```

---

## 📁 Padrão Estrutural por Disciplina

Cada componente curricular é organizado nas seguintes seções:
- `Aulas/`: Aulas modulares numeradas (`Aula_01/`, `Aula_02/`, ...), cada uma com código de apoio, materiais/slides e guia de estudos.
- `Avaliacoes/`: Provas teóricas (AVT), avaliações práticas de laboratório (AVP) e listas de exercícios avaliativas.
- `Referencias/`: Ementas oficiais, planos de ensino (PUD), livros, artigos e modelos de slides Beamer.
- `README.md`: Documentação e identificação completa da disciplina com cronograma semestral.
