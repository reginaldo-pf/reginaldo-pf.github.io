"""
settings.py - Constantes globais e parâmetros de jogabilidade.
Contém configurações de tela, física precisa de Mega Man X, cores e controles.
"""

import pygame

# Resolução da tela
# Usamos uma resolução interna retrô (16:9) escalada com escala limpa
INTERNAL_WIDTH = 640
INTERNAL_HEIGHT = 360
WINDOW_SCALE = 2  # Janela de 1280x720 na tela
SCREEN_WIDTH = INTERNAL_WIDTH * WINDOW_SCALE
SCREEN_HEIGHT = INTERNAL_HEIGHT * WINDOW_SCALE
FPS = 60
TILE_SIZE = 32

# Paleta de Cores (Estilo 16-bits Super Nintendo)
COLOR_BG = (16, 20, 32)
COLOR_GRID = (28, 36, 56)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# Cores do X (Mega Man)
COLOR_X_CYAN = (0, 230, 240)
COLOR_X_BLUE = (0, 80, 200)
COLOR_X_DARK_BLUE = (0, 40, 120)
COLOR_X_WHITE = (240, 245, 255)
COLOR_X_RED = (235, 45, 45)
COLOR_X_GOLD = (255, 215, 0)
COLOR_X_FLESH = (255, 205, 170)

# Cores de Efeitos e Tiros
COLOR_BUSTER_NORMAL = (255, 240, 80)
COLOR_BUSTER_CHARGE_1 = (50, 255, 100)
COLOR_BUSTER_CHARGE_2 = (0, 220, 255)
COLOR_BUSTER_CHARGE_PINK = (255, 70, 190)

# Cores de Inimigos e Cenário
COLOR_ENEMY_YELLOW = (250, 210, 30)
COLOR_ENEMY_DARK = (45, 45, 55)
COLOR_ENEMY_RED = (230, 40, 40)
COLOR_BOSS_PURPLE = (140, 40, 190)
COLOR_BOSS_GOLD = (230, 180, 20)
COLOR_BOSS_STEEL = (110, 125, 145)

COLOR_TILE_METAL = (75, 90, 115)
COLOR_TILE_TOP = (110, 130, 160)
COLOR_TILE_ACCENT = (0, 190, 210)
COLOR_SPIKE = (220, 40, 40)

# Física do Jogador (Ajustada com o "feeling" do Mega Man X do SNES)
PLAYER_SPEED = 190.0           # Velocidade horizontal ao correr (pixels/segundo)
PLAYER_DASH_SPEED = 340.0      # Velocidade do Dash (1.8x da corrida)
PLAYER_DASH_DURATION = 0.36    # Duração do dash em segundos
PLAYER_DASH_COOLDOWN = 0.15    # Intervalo mínimo entre dashes
PLAYER_GRAVITY = 950.0         # Aceleração gravitacional
PLAYER_MAX_FALL_SPEED = 480.0  # Velocidade terminal de queda
PLAYER_JUMP_FORCE = -400.0     # Impulso inicial do pulo
PLAYER_JUMP_CUTOFF = -140.0    # Velocidade mínima ao soltar botão de pulo (pulo variável)
PLAYER_WALL_SLIDE_SPEED = 85.0 # Velocidade reduzida ao deslizar na parede
PLAYER_WALL_JUMP_X = 260.0     # Impulso horizontal ao quicar na parede
PLAYER_WALL_JUMP_Y = -380.0    # Impulso vertical ao quicar na parede
PLAYER_WALL_JUMP_LOCK = 0.16   # Tempo que o controle direcional fica travado após o kick

# Combate
PLAYER_MAX_HP = 16
PLAYER_INVINCIBILITY_TIME = 1.2 # Tempo piscando após levar dano
CHARGE_LEVEL_1_TIME = 0.55     # Tempo para atingir carga média
CHARGE_LEVEL_2_TIME = 1.30     # Tempo para carga máxima

# Balanço de Dano dos Tiros
DAMAGE_BUSTER_NORMAL = 1
DAMAGE_BUSTER_CHARGE_1 = 3
DAMAGE_BUSTER_CHARGE_2 = 6

# Mapeamento de Controles (Suporta Setas e WASD)
KEY_LEFT = (pygame.K_LEFT, pygame.K_a)
KEY_RIGHT = (pygame.K_RIGHT, pygame.K_d)
KEY_UP = (pygame.K_UP, pygame.K_w)
KEY_DOWN = (pygame.K_DOWN, pygame.K_s)
KEY_JUMP = (pygame.K_SPACE, pygame.K_z, pygame.K_k)
KEY_SHOOT = (pygame.K_x, pygame.K_j)
KEY_DASH = (pygame.K_c, pygame.K_LSHIFT, pygame.K_l)
KEY_PAUSE = (pygame.K_ESCAPE, pygame.K_p)
KEY_START = (pygame.K_RETURN, pygame.K_SPACE)
