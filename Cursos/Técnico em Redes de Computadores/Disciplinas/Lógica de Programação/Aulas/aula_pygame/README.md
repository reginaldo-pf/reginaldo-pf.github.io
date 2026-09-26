# Aula Introdutória: Desenvolvimento de Jogos 2D com Pygame

Material didático completo, estruturado e testado para aula de **90 minutos (1h 30min)** no curso de **Análise e Desenvolvimento de Sistemas (ADS)** do **IFCE Campus Tauá**.

*   **Professor:** Prof. Reginaldo Fernandes
*   **Biblioteca:** `pygame-ce` (Python 3.10+)

---

## 📁 Estrutura de Arquivos da Aula

```text
aula_pygame/
├── README.md                                 # Este guia de orientação rápida
├── plano_de_aula.md                          # Plano de aula minuto a minuto (90 min)
├── slides/                                   # Apresentação LaTeX Beamer modular
│   ├── main.tex                              # Arquivo mestre dos slides
│   ├── main.pdf                              # PDF compilado pronto para apresentação
│   ├── secao1_introducao.tex                 # O que é Pygame e arquitetura de jogos
│   ├── secao2_game_loop.tex                  # A anatomia do Game Loop (Ciclo de 4 fases)
│   ├── secao3_coordenadas_e_cores.tex        # Origem (0,0), Y invertido e cores RGB
│   ├── secao4_movimento_e_tempo.tex          # Física básica, tela.fill() e clock.tick()
│   ├── secao5_colisoes_e_jogo.tex            # pygame.Rect, colliderect() e textos (HUD)
│   └── secao6_exercicios_conclusao.tex       # Laboratório prático e desafios
└── exemplos/                                 # Códigos didáticos progressivos
    ├── 01_janela_e_game_loop.py              # Esqueleto essencial do Pygame
    ├── 02_coordenadas_e_formas.py            # Formas geométricas e mouse em tempo real
    ├── 03_animacao_e_fps.py                  # Movimento, controle de FPS e efeito rastro
    ├── 04_controles_e_bordas.py              # Movimento contínuo e contenção nas bordas
    ├── 05_mini_jogo_coleta.py                # Jogo integrador: "Caça aos Cristais"
    └── exercicios/                           # Desafios para a turma
        ├── desafio1_bola_quicando.py         # Exercício 1 (Bouncing Ball)
        ├── desafio2_esquiva_obstaculo.py     # Exercício 2 (Dodge Obstacles)
        └── solucoes/                         # Códigos comentados com as resoluções
            ├── desafio1_resolvido.py
            └── desafio2_resolvido.py
```

---

## 🚀 Como Executar os Exemplos

Todos os scripts utilizam o ambiente virtual já configurado com `pygame-ce`. Para executar qualquer exemplo pelo terminal na raiz do projeto:

```bash
# Exemplo 1: Esqueleto e Game Loop
.venv/bin/python3 aula_pygame/exemplos/01_janela_e_game_loop.py

# Exemplo 2: Coordenadas e Primitivos Gráficos (Mova o mouse!)
.venv/bin/python3 aula_pygame/exemplos/02_coordenadas_e_formas.py

# Exemplo 3: Animação e FPS (Pressione [ESPAÇO] e [F] para testar)
.venv/bin/python3 aula_pygame/exemplos/03_animacao_e_fps.py

# Exemplo 4: Controles por Teclado e Bloqueio de Bordas
.venv/bin/python3 aula_pygame/exemplos/04_controles_e_bordas.py

# Exemplo 5: Projeto Integrador Completo ("Caça aos Cristais")
.venv/bin/python3 aula_pygame/exemplos/05_mini_jogo_coleta.py
```

---

## 📽️ Slides da Apresentação

O arquivo compilado [aula_pygame/slides/main.pdf](slides/main.pdf) contém 19 slides formatados sob o tema Beamer Madrid/Whale, contendo diagramas conceituais em TikZ, caixas de código Python coloridas e tabelas comparativas.

Caso faça alterações nos arquivos `.tex`, recompile os slides executando:

```bash
cd aula_pygame/slides && pdflatex -interaction=nonstopmode main.tex
```
