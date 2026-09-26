# Plano de Aula: Introdução ao Desenvolvimento de Jogos 2D com Pygame

*   **Disciplina / Módulo:** Programação de Computadores / Lógica e Prática de Jogos 2D
*   **Público-Alvo:** Graduação em Tecnologia em Análise e Desenvolvimento de Sistemas (ADS) / Técnico Integrado (IFCE Campus Tauá)
*   **Professor Responsável:** Prof. Reginaldo Fernandes
*   **Duração Planejada:** 90 minutos (2 horas-aula completas de laboratório)
*   **Ambiente Necessário:** Laboratório de Informática com Python 3.10+ e `pygame-ce` instalado.

---

## 🎯 1. Objetivos de Aprendizagem

### Objetivo Geral
Compreender a arquitetura de software de aplicações gráficas em tempo real, dominando o funcionamento interno da biblioteca **Pygame** através da construção prática de um jogo 2D interativo com entrada de teclado, física básica, colisões e controle de taxa de quadros.

### Objetivos Específicos
Ao término desta aula, o estudante será capaz de:
1.  **Diferenciar** o modelo computacional orientado a eventos tradicional (requisições/pausas) do modelo contínuo em tempo real (*Game Loop*).
2.  **Identificar e programar** as quatro etapas vitais do *Game Loop*: Polling de Eventos, Atualização Lógica, Renderização Gráfica e Sincronização do Relógio.
3.  **Mapear posições** no sistema de coordenadas cartesiano de tela (Origem no Top-Left e Eixo Y invertido para baixo) e manipular cores aditivas em tuplas RGB $(0 \dots 255)$.
4.  **Explicar a necessidade** do *Double Buffering* (`display.flip()`), da limpeza de tela periódica (`fill()`) e da trava de quadros por segundo (`Clock.tick(FPS)`).
5.  **Capturar comandos do jogador** com fluidez utilizando estados de teclas contínuos (`pygame.key.get_pressed()`) e aplicar restrição de limites (*Border Clamping*).
6.  **Calcular colisões geométricas** 2D entre retângulos (*Axis-Aligned Bounding Box - AABB*) através do método `colliderect()` do `pygame.Rect`.
7.  **Renderizar interfaces de usuário (HUD)** utilizando fontes do sistema (`pygame.font.SysFont`) e transferência de blocos de pixels (`blit`).

---

## ⏰ 2. Cronograma Detalhado da Aula (90 Minutos)

| Bloco | Tempo | Fase Didática | Conteúdo e Metodologia |
| :---: | :---: | :--- | :--- |
| **B1** | **00 – 15 min** | **Problematização & Arquitetura** | • Comparação: Aplicação Web/CLI vs.\ Jogo em Tempo Real.<br>• O que é Pygame e SDL.<br>• Apresentação do diagrama cíclico do **Game Loop**.<br>• *Demonstração ao vivo:* [01_janela_e_game_loop.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/01_janela_e_game_loop.py). |
| **B2** | **15 – 30 min** | **Espaço Gráfico 2D & Cores** | • O plano cartesiano com Y invertido (origem no canto superior esquerdo).<br>• Modelo de cores aditivo RGB (0 a 255).<br>• Desenho vetorial primitivo com `pygame.draw` (retângulos, círculos, linhas).<br>• *Demonstração ao vivo:* [02_coordenadas_e_formas.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/02_coordenadas_e_formas.py) (com rastreador de mouse em tempo real). |
| **B3** | **30 – 45 min** | **Física, Rastro & Tempo (FPS)** | • Animação passo a passo: $x \leftarrow x + v_x$.<br>• O problema clássico do "rastro infinito" e a função `tela.fill()`.<br>• O papel do `pygame.time.Clock()` e cálculo do $\Delta t$ ($16{,}6\text{ ms}$).<br>• *Demonstração ao vivo:* [03_animacao_e_fps.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/03_animacao_e_fps.py) (alternando rastro com [ESPAÇO] e FPS com [F]). |
| **B4** | **45 – 60 min** | **Interatividade & Controles** | • Fila de eventos vs.\ Estado contínuo (`KEYDOWN` vs.\ `key.get_pressed`).<br>• Controle fluido com Setas e WASD.<br>• Bloqueio contra saída da tela (*Border Clamping*).<br>• *Demonstração ao vivo:* [04_controles_e_bordas.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/04_controles_e_bordas.py). |
| **B5** | **60 – 75 min** | **Colisões (Rect) & Mini-Jogo** | • A classe `pygame.Rect` e geometria AABB.<br>• Colisão automática com `colliderect()`.<br>• Textos na tela: Fontes do sistema e função `blit()`.<br>• *Demonstração ao vivo:* [05_mini_jogo_coleta.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/05_mini_jogo_coleta.py) ("Caça aos Cristais"). |
| **B6** | **75 – 90 min** | **Prática Guiada & Desafios** | • Alunos abrem os arquivos da pasta `exercicios/` no computador do laboratório.<br>• Resolução assistida do Desafio 1 (Bouncing Ball) ou Desafio 2 (Dodge Obstacles).<br>• Síntese dos pilares, feedback e encerramento. |

---

## 🛝 3. Roteiro Slide a Slide (Slides LaTeX Beamer)

A apresentação correspondente está compilada e pronta para exibição em [aula_pygame/slides/main.pdf](file:///home/reginaldo-fernandes/logica/aula_pygame/slides/main.pdf). Abaixo estão as diretrizes pedagógicas para cada slide:

### Slide 1 a 2: Abertura e Sumário
*   **Ação do Professor:** Apresentar a ementa da aula e motivar a turma explicando que os mesmos fundamentos aprendidos hoje regem desde jogos 2D clássicos até engines industriais (Godot, Unity, Unreal).

### Slide 3 a 4: Seção 1 -- Introdução e Filosofia do Pygame
*   **Pontos-Chave:** O Pygame é um *wrapper* sobre a biblioteca multiplataforma SDL em C.
*   **Nota do Professor:** Destaque a diferença filosófica: "Em um script de terminal, o código pausa no `input()`. Em um jogo, se o jogador largar o teclado, os inimigos continuam andando e a física continua agindo. O processador nunca para de executar o laço!"
*   **Elemento Visual:** Caixa comparativa (Aplicações Tradicionais vs.\ Jogos em Tempo Real).

### Slide 5 a 7: Seção 2 -- A Anatomia do Game Loop
*   **Pontos-Chave:** As 4 fases cíclicas: Eventos $\rightarrow$ Lógica $\rightarrow$ Desenho $\rightarrow$ Relógio.
*   **Nota do Professor:** Mostre o código esqueleto básico. Faça a pergunta reflexiva: *"O que acontece se comentarmos a linha `pygame.event.get()`?"* Mostre que o sistema operacional congela a janela com "Programa não está respondendo" porque a fila do SO transbordou.
*   **Elemento Visual:** Diagrama vetorial TikZ com as quatro caixas interconectadas.

### Slide 8 a 10: Seção 3 -- Coordenadas 2D e Cores RGB
*   **Pontos-Chave:** Top-Left é $(0, 0)$. O eixo Y aponta para baixo. As cores são tuplas $(R, G, B)$ de $0$ a $255$.
*   **Nota do Professor:** Este é o maior ponto de confusão para quem veio da matemática do ensino médio. Enfatize: "Para pular para cima, você precisa SUBTRAIR da posição Y!".
*   **Elemento Visual:** Gráfico com a janela e eixos $+X$ (horizontal direito) e $+Y$ (vertical descendente).

### Slide 11 a 13: Seção 4 -- Animação, FPS e Interatividade
*   **Pontos-Chave:** $x = x + v$. O erro do rastro quando não há `tela.fill()`. O papel do `clock.tick(60)` para evitar queima de CPU e velocidade disparada.
*   **Nota do Professor:** Execute o script [03_animacao_e_fps.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/03_animacao_e_fps.py). Aperte a barra de espaço para desligar o `fill()` e deixe a turma ver a bolinha "pintar" a tela. Esse impacto visual fixa o conceito instantaneamente.

### Slide 14 a 16: Seção 5 -- Colisões com pygame.Rect e o Mini-Jogo
*   **Pontos-Chave:** Propriedades convenientes do `pygame.Rect` (`top`, `bottom`, `left`, `right`, `center`). A matemática do teste AABB. O método `rect1.colliderect(rect2)`. O pipeline de texto: `SysFont` $\rightarrow$ `render` $\rightarrow$ `blit`.
*   **Nota do Professor:** Execute o jogo completo [05_mini_jogo_coleta.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/05_mini_jogo_coleta.py). Mostre como todos os conceitos vistos (loop, cores, coordenadas, teclado, colisões e texto) se unem harmonicamente em menos de 150 linhas de código.

### Slide 17 a 19: Seção 6 -- Laboratório Prático e Conclusão
*   **Pontos-Chave:** Orientações para a atividade de laboratório e visão de futuro (Sprites, Spritesheets, POO e Física avançada).

---

## 🛠️ 4. Guia dos Scripts Didáticos de Apoio

Todos os scripts estão prontos para execução no diretório [aula_pygame/exemplos/](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/):

1.  **[01_janela_e_game_loop.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/01_janela_e_game_loop.py):**
    *   *Objetivo:* Explicar a estrutura mínima com clareza cristalina.
    *   *Comando:* `python3 aula_pygame/exemplos/01_janela_e_game_loop.py`
2.  **[02_coordenadas_e_formas.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/02_coordenadas_e_formas.py):**
    *   *Objetivo:* Mostrar formas vetoriais e exibir as coordenadas $(X, Y)$ do cursor do mouse em tempo real na tela.
    *   *Comando:* `python3 aula_pygame/exemplos/02_coordenadas_e_formas.py`
3.  **[03_animacao_e_fps.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/03_animacao_e_fps.py):**
    *   *Objetivo:* Demonstrar a física do rebote em paredes, o efeito do rastro sem limpeza de tela (pressione `[ESPAÇO]`) e o limitador de FPS (pressione `[F]`).
    *   *Comando:* `python3 aula_pygame/exemplos/03_animacao_e_fps.py`
4.  **[04_controles_e_bordas.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/04_controles_e_bordas.py):**
    *   *Objetivo:* Ensinar movimentação de personagens pelo teclado contínuo e contenção dentro dos limites da janela (*clamping*).
    *   *Comando:* `python3 aula_pygame/exemplos/04_controles_e_bordas.py`
5.  **[05_mini_jogo_coleta.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/05_mini_jogo_coleta.py):**
    *   *Objetivo:* Projeto integrador completo ("Caça aos Cristais") com itens coletáveis, armadilha em movimento, sons procedurais em tempo real e tela de Game Over.
    *   *Comando:* `python3 aula_pygame/exemplos/05_mini_jogo_coleta.py`

---

## ⚠️ 5. Guia de Diagnóstico de Erros Comuns dos Alunos

Durante a prática de laboratório, os alunos costumam cometer erros típicos. Use esta tabela rápida para diagnóstico e intervenção pedagógica:

| Sintoma Observado | Causa Mais Provável | Correção Rápida |
| :--- | :--- | :--- |
| **Janela congela com mensagem "Não respondendo"** | Falta o laço de eventos com `pygame.event.get()`. | Incluir o bloco `for evento in pygame.event.get(): if evento.type == pygame.QUIT: ...` |
| **A tela fica totalmente preta e nada aparece** | O aluno desenhou as formas mas esqueceu o `pygame.display.flip()`. | Adicionar `pygame.display.flip()` ao final da fase de desenho. |
| **O objeto em movimento deixa um rastro borrado** | Esqueceu de chamar `tela.fill(COR)` a cada quadro. | Inserir `tela.fill(COR_FUNDO)` antes de qualquer chamada a `pygame.draw`. |
| **O personagem move-se em velocidade absurda** | Falta o `relogio.tick(60)` dentro do `while`. | Instanciar `relogio = pygame.time.Clock()` e chamar `relogio.tick(60)` ao fim do loop. |
| **Ao pressionar para cima, o personagem desce** | O aluno somou em vez de subtrair na coordenada Y. | Corrigir para `pos_y -= velocidade` quando a tecla de subir for pressionada. |
| **O personagem anda "aos trancos"** | Usou o evento pontual `pygame.KEYDOWN` para andar. | Usar `teclas = pygame.key.get_pressed()` para movimentação contínua. |

---

## 📝 6. Exercícios de Laboratório (Com Solução)

Os exercícios estão disponíveis com marcações `# TODO` para os alunos preencherem:

1.  **Desafio 1: A Bola Quicante com Cores Dinâmicas**
    *   *Arquivo do Aluno:* [aula_pygame/exemplos/exercicios/desafio1_bola_quicando.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/exercicios/desafio1_bola_quicando.py)
    *   *Arquivo de Gabarito:* [aula_pygame/exemplos/exercicios/solucoes/desafio1_resolvido.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/exercicios/solucoes/desafio1_resolvido.py)
    *   *Competência avaliada:* Detecção de bordas e alteração de variáveis de velocidade e cor.

2.  **Desafio 2: Esquiva de Obstáculos (Dodge)**
    *   *Arquivo do Aluno:* [aula_pygame/exemplos/exercicios/desafio2_esquiva_obstaculo.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/exercicios/desafio2_esquiva_obstaculo.py)
    *   *Arquivo de Gabarito:* [aula_pygame/exemplos/exercicios/solucoes/desafio2_resolvido.py](file:///home/reginaldo-fernandes/logica/aula_pygame/exemplos/exercicios/solucoes/desafio2_resolvido.py)
    *   *Competência avaliada:* Manipulação de listas de `pygame.Rect`, movimentação vertical descendente contínua e colisão com o jogador usando `colliderect`.
