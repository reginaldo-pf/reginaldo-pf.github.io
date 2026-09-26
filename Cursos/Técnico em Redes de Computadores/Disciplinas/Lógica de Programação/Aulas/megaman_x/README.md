# Mega Man X - Projeto Final de Programação

Um jogo completo estilo plataforma de ação 2D inspirado no clássico **Mega Man X** (Super Nintendo), desenvolvido em **Python** utilizando a biblioteca **`pygame-ce`**.

Este projeto foi desenhado como um modelo exemplar para disciplinas acadêmicas de **Lógica de Programação**, **Programação Orientada a Objetos (POO)** e **Desenvolvimento de Jogos**, demonstrando boas práticas de engenharia de software, modularidade e desacoplamento.

---

## 🎮 Funcionalidades e Mecânicas Implementadas

### 1. Física e Movimentação Fiel ao SNES
* **Corrida & Inércia**: Movimento horizontal suave e responsivo.
* **Pulo Variável**: O impulso de subida é proporcional ao tempo que o jogador mantém o botão pressionado (soltar a tecla corta o impulso vertical suavemente).
* **Dash**: Investida em alta velocidade (`340 px/s`) por tempo limitado (`0.36s`) com fumaça e rastro translúcido (*ghost trail*).
* **Dash Jump**: Ao pular durante um Dash, o jogador preserva a velocidade máxima no ar até tocar o chão novamente.
* **Wall Slide**: Ao encostar em uma parede durante uma queda e segurar a direção, o jogador desliza lentamente emitindo faíscas de atrito.
* **Wall Jump / Wall Kick**: Impulso diagonal quicando na parede oposta, permitindo escalar poços e desviar de ataques.

### 2. Sistema de Armamento (Mega Buster)
* **Nível 0 (Tiro Normal)**: Pequenos projéteis rápidos de plasma (limite de 3 simultâneos).
* **Nível 1 (Carga Média - 0.55s)**: Esfera de plasma verde com dano triplicado.
* **Nível 2 (Carga Máxima - 1.30s)**: Disparo massivo espiral ciano/magenta com efeito perfurante e tremor de tela (*screen shake*).
* **Aura de Carga**: Partículas coloridas convergem para o X enquanto o botão de tiro é mantido pressionado.

### 3. Inimigos e Inteligência Artificial
* **Metool (Metall)**:
  * Permanece escondido sob seu capacete blindado (imune a tiros normais; vulnerável apenas a tiros de carga máxima ou quando se levanta).
  * Levanta-se periodicamente, caminha e dispara 3 tiros em leque.
* **Batton**:
  * Fica camuflado no teto com as asas fechadas (alta defesa).
  * Quando o jogador se aproxima, abre as asas e voa em curva senoidal em sua direção.
* **Gunner Turret**:
  * Torreta sentinela que calcula o ângulo em direção ao jogador e dispara projéteis balísticos regulares.
* **Chefe da Fase (Maverick Rex)**:
  * Possui barra de vida vertical própria que se preenche na introdução com alarme sonoro.
  * Máquina de estados com ataques dinâmicos: *Dash Stomp*, *Salto com Terremoto*, *Disparo Triplo de Plasma*.
  * Efeito de explosões sequenciais e fanfarra de vitória (*Stage Clear*).

### 4. Áudio & Gráficos 100% Autônomos (Zero Dependências Externas)
* **Áudio Procedural**: Todos os efeitos sonoros (tiros, saltos, explosões, alarmes e fanfarra) são sintetizados matematicamente via código PCM mono (sem necessitar de arquivos `.wav` ou `.mp3` externos).
* **Pixel Art Procedural**: Spritesheets de 16-bits desenhados programaticamente com precisão de pixels.

---

## ⌨️ Controles do Jogo

| Ação | Teclas Primárias | Teclas Alternativas |
| :--- | :--- | :--- |
| **Mover para Esquerda / Direita** | `←` / `→` | `A` / `D` |
| **Pular / Quicar na Parede** | `Espaço` | `Z` ou `K` |
| **Atirar / Carregar Buster** | `X` *(segure para carregar)* | `J` |
| **Dash (Investida)** | `C` | `Shift Esquerdo` ou `L` |
| **Iniciar / Reiniciar** | `Enter` | `Espaço` |
| **Sair** | `ESC` | Fechar Janela |

---

## 📁 Arquitetura do Código

```text
megaman_x/
├── main.py              # Loop de jogo principal, máquina de estados da aplicação e upscale
├── run.sh               # Script de execução rápida
├── requirements.txt     # Dependências (pygame-ce)
├── README.md            # Documentação técnica e acadêmica
└── src/
    ├── settings.py      # Resoluções, cores 16-bits e constantes de física
    ├── audio.py         # Síntese matemática de áudio (SFX retrô)
    ├── sprites.py       # Renderização de pixel-art em superfícies Pygame
    ├── particles.py     # Sistema de partículas (dash dust, aura de carga, fagulhas)
    ├── camera.py        # Câmera 2D com interpolação suave (lerp) e screen shake
    ├── bullet.py        # Classes de projéteis (Buster simples, carregado e tiros inimigos)
    ├── player.py        # Física, máquina de estados e combate do protagonista X
    ├── enemies.py       # Inimigos comuns, chefes com IA e itens coletáveis
    ├── level.py         # Mapa de tiles ASCII, detecção de colisões e perigos
    └── ui.py            # HUD clássico, barras verticais segmentadas e telas
```

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3.10 ou superior
* Biblioteca `pygame-ce`

### Passo 1: Instalação das dependências
Se estiver utilizando ambiente virtual (venv):
```bash
pip install -r requirements.txt
```

### Passo 2: Executar o jogo
Você pode rodar diretamente com o script fornecido:
```bash
./run.sh
```
Ou executando o arquivo principal com o interpretador Python:
```bash
python3 main.py
```

---

## 🎓 Conceitos Acadêmicos Demonstrados

1. **Abstração & Encapsulamento**: Cada subsistema gerencia seu próprio estado interno sem vazamento de escopo.
2. **Herança & Polimorfismo**:
   * `Enemy` serve de classe base abstrata para `Metool`, `Batton`, `GunnerTurret` e `MaverickBoss`.
   * `Bullet` serve de base para `BusterBullet`, `EnemyBullet` e `BossBullet`.
3. **Máquinas de Estado Finitas (FSM)**:
   * Estados do Jogador: `IDLE`, `RUN`, `JUMP`, `FALL`, `DASH`, `WALL_SLIDE`, `HURT`.
   * Estados do Chefe: `INTRO`, `IDLE`, `DASH_ATTACK`, `JUMP_STOMP`, `TRIPLE_PLASMA`, `DYING`.
4. **Física de Jogos 2D**:
   * Integração de Euler para velocidade e aceleração por Delta Time (`dt`).
   * Resolução de colisão desacoplada em eixos separados ($X$ e $Y$) para prevenção de penetração em quinas (*tunneling*).
5. **Double Buffering e Virtual Resolution**:
   * Renderização em resolução interna nativa de 640x360 (proporção 16:9) com escala limpa para janela em alta definição (1280x720).
