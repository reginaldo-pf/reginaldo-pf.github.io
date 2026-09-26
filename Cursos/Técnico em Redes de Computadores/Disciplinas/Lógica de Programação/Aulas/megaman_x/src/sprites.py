"""
sprites.py - Gerador procedural de sprites pixel-art em estilo 16-bits.
Gera os spritesheets do jogador (X), inimigos, chefe, projéteis, tiles e itens
diretamente em superfícies do Pygame, eliminando dependências externas.
"""

import pygame
from .settings import (
    COLOR_X_CYAN, COLOR_X_BLUE, COLOR_X_DARK_BLUE, COLOR_X_WHITE,
    COLOR_X_RED, COLOR_X_GOLD, COLOR_X_FLESH, COLOR_BLACK, COLOR_WHITE,
    COLOR_BUSTER_NORMAL, COLOR_BUSTER_CHARGE_1, COLOR_BUSTER_CHARGE_2,
    COLOR_BUSTER_CHARGE_PINK, COLOR_ENEMY_YELLOW, COLOR_ENEMY_DARK,
    COLOR_ENEMY_RED, COLOR_BOSS_PURPLE, COLOR_BOSS_GOLD, COLOR_BOSS_STEEL,
    COLOR_TILE_METAL, COLOR_TILE_TOP, COLOR_TILE_ACCENT, COLOR_SPIKE,
    TILE_SIZE
)

def create_pixel_surface(w, h):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((0, 0, 0, 0))
    return surf

class SpriteFactory:
    _instance = None

    def __init__(self):
        self.player_sprites = {}
        self.enemy_sprites = {}
        self.bullet_sprites = {}
        self.tile_sprites = {}
        self.item_sprites = {}
        self._generate_all()

    @classmethod
    def get(cls):
        if cls._instance is None:
            cls._instance = SpriteFactory()
        return cls._instance

    def _generate_all(self):
        self._build_player_sprites()
        self._build_enemy_sprites()
        self._build_bullet_sprites()
        self._build_tile_sprites()
        self._build_item_sprites()

    # -------------------------------------------------------------
    # JOGADOR (X)
    # -------------------------------------------------------------
    def _draw_x_base(self, surf, ox, oy, pose="idle", frame=0, shooting=False):
        """Desenha a silhueta clássica de Mega Man X em uma superfície."""
        # Dimensões aproximadas: 28 de largura, 34 de altura
        c_cyan = COLOR_X_CYAN
        c_blue = COLOR_X_BLUE
        c_dblue = COLOR_X_DARK_BLUE
        c_white = COLOR_X_WHITE
        c_red = COLOR_X_RED
        c_skin = COLOR_X_FLESH
        c_gold = COLOR_X_GOLD

        # Ajuste de altura para respiração ou agachamento
        y_off = oy
        if pose == "idle" and frame == 1:
            y_off += 1
        elif pose == "dash":
            y_off += 8  # Agachado no dash

        # Pernas e Botas
        if pose == "dash":
            # Posição inclinada de sprint
            pygame.draw.rect(surf, c_blue, (ox + 4, y_off + 12, 18, 6))
            pygame.draw.rect(surf, c_cyan, (ox + 16, y_off + 14, 10, 8))
            pygame.draw.rect(surf, c_dblue, (ox + 2, y_off + 14, 10, 8))
            # Fogo do propulsor atrás dos pés
            pygame.draw.polygon(surf, (255, 200, 50), [(ox, y_off + 16), (ox - 6, y_off + 18), (ox, y_off + 20)])
            pygame.draw.polygon(surf, c_cyan, [(ox - 2, y_off + 17), (ox - 8, y_off + 18), (ox - 2, y_off + 19)])
        elif pose == "jump" or pose == "fall":
            # Pernas dobradas no ar
            pygame.draw.rect(surf, c_dblue, (ox + 6, y_off + 18, 5, 8))
            pygame.draw.rect(surf, c_cyan, (ox + 4, y_off + 24, 8, 7))
            pygame.draw.rect(surf, c_blue, (ox + 14, y_off + 17, 5, 6))
            pygame.draw.rect(surf, c_cyan, (ox + 15, y_off + 21, 8, 7))
        elif pose == "wall_slide":
            # Agarrado à parede
            pygame.draw.rect(surf, c_dblue, (ox + 10, y_off + 18, 6, 6))
            pygame.draw.rect(surf, c_cyan, (ox + 12, y_off + 24, 8, 8))
            pygame.draw.rect(surf, c_white, (ox + 18, y_off + 29, 3, 3))
        elif pose == "run":
            # 4 frames de corrida
            offsets = [(2, 22, 14, 22), (4, 20, 12, 24), (12, 22, 4, 22), (14, 24, 2, 20)]
            lx, ly, rx, ry = offsets[frame % 4]
            pygame.draw.rect(surf, c_cyan, (ox + lx, y_off + ly, 7, 10))
            pygame.draw.rect(surf, c_cyan, (ox + rx, y_off + ry, 7, 10))
            pygame.draw.rect(surf, c_dblue, (ox + 8, y_off + 16, 8, 6))
        else: # idle
            # Pernas paradas firmes
            pygame.draw.rect(surf, c_dblue, (ox + 7, y_off + 16, 10, 6))
            pygame.draw.rect(surf, c_cyan, (ox + 5, y_off + 21, 7, 11))
            pygame.draw.rect(surf, c_cyan, (ox + 13, y_off + 21, 7, 11))
            pygame.draw.rect(surf, c_white, (ox + 5, y_off + 29, 6, 3))
            pygame.draw.rect(surf, c_white, (ox + 14, y_off + 29, 6, 3))

        # Tronco e Peitoral
        if pose == "dash":
            pygame.draw.rect(surf, c_blue, (ox + 8, y_off + 6, 14, 8))
            pygame.draw.rect(surf, c_cyan, (ox + 10, y_off + 7, 10, 6))
            pygame.draw.rect(surf, c_white, (ox + 13, y_off + 8, 4, 4))
        elif pose == "wall_slide":
            pygame.draw.rect(surf, c_blue, (ox + 6, y_off + 8, 12, 10))
            pygame.draw.rect(surf, c_cyan, (ox + 8, y_off + 9, 8, 8))
        else:
            pygame.draw.rect(surf, c_blue, (ox + 7, y_off + 8, 11, 9))
            pygame.draw.rect(surf, c_cyan, (ox + 8, y_off + 9, 9, 7))
            pygame.draw.rect(surf, c_white, (ox + 10, y_off + 10, 5, 5))

        # Cabeça e Capacete de Mega Man X
        hx = ox + 7 if pose != "dash" else ox + 12
        hy = y_off - 1 if pose != "dash" else y_off + 1

        # Capacete azul e ciano
        pygame.draw.rect(surf, c_blue, (hx, hy, 12, 10))
        pygame.draw.rect(surf, c_cyan, (hx + 2, hy, 8, 3))
        # Rosto (pele)
        pygame.draw.rect(surf, c_skin, (hx + 4, hy + 3, 7, 6))
        # Olho
        pygame.draw.rect(surf, COLOR_BLACK, (hx + 8, hy + 4, 2, 3))
        pygame.draw.rect(surf, c_white, (hx + 8, hy + 4, 1, 2))
        # Cristal vermelho na testa
        pygame.draw.rect(surf, c_red, (hx + 5, hy + 1, 3, 2))
        # Módulo de orelha dourado
        pygame.draw.rect(surf, c_gold, (hx + 1, hy + 4, 2, 4))

        # Braço e Buster
        if shooting:
            # Buster estendido para frente
            bx = ox + 18 if pose != "dash" else ox + 22
            by = y_off + 9 if pose != "dash" else y_off + 7
            pygame.draw.rect(surf, c_blue, (bx, by, 10, 6))
            pygame.draw.rect(surf, c_cyan, (bx + 3, by + 1, 6, 4))
            pygame.draw.rect(surf, (255, 240, 80), (bx + 9, by + 2, 2, 2))  # Brilho do cano
        elif pose == "wall_slide":
            # Braço estendido segurando na parede
            pygame.draw.rect(surf, c_cyan, (ox + 16, y_off + 6, 6, 8))
        elif pose == "dash":
            pygame.draw.rect(surf, c_cyan, (ox + 6, y_off + 8, 8, 5))
        else:
            # Braço relaxado ao lado
            pygame.draw.rect(surf, c_cyan, (ox + 4, y_off + 9, 4, 8))

    def _build_player_sprites(self):
        w, h = 32, 36
        # Idle (2 frames)
        self.player_sprites["idle"] = []
        for f in range(2):
            s = create_pixel_surface(w, h)
            self._draw_x_base(s, 2, 2, "idle", f, shooting=False)
            self.player_sprites["idle"].append(s)

        # Idle Shooting
        self.player_sprites["idle_shoot"] = create_pixel_surface(w, h)
        self._draw_x_base(self.player_sprites["idle_shoot"], 2, 2, "idle", 0, shooting=True)

        # Run (4 frames)
        self.player_sprites["run"] = []
        for f in range(4):
            s = create_pixel_surface(w, h)
            self._draw_x_base(s, 2, 2, "run", f, shooting=False)
            self.player_sprites["run"].append(s)

        # Run Shooting (4 frames)
        self.player_sprites["run_shoot"] = []
        for f in range(4):
            s = create_pixel_surface(w, h)
            self._draw_x_base(s, 2, 2, "run", f, shooting=True)
            self.player_sprites["run_shoot"].append(s)

        # Jump & Fall
        self.player_sprites["jump"] = create_pixel_surface(w, h)
        self._draw_x_base(self.player_sprites["jump"], 2, 2, "jump", 0, shooting=False)

        self.player_sprites["jump_shoot"] = create_pixel_surface(w, h)
        self._draw_x_base(self.player_sprites["jump_shoot"], 2, 2, "jump", 0, shooting=True)

        self.player_sprites["fall"] = create_pixel_surface(w, h)
        self._draw_x_base(self.player_sprites["fall"], 2, 2, "fall", 0, shooting=False)

        # Dash
        self.player_sprites["dash"] = create_pixel_surface(w, h)
        self._draw_x_base(self.player_sprites["dash"], 2, 2, "dash", 0, shooting=False)

        self.player_sprites["dash_shoot"] = create_pixel_surface(w, h)
        self._draw_x_base(self.player_sprites["dash_shoot"], 2, 2, "dash", 0, shooting=True)

        # Wall Slide
        self.player_sprites["wall_slide"] = create_pixel_surface(w, h)
        self._draw_x_base(self.player_sprites["wall_slide"], 2, 2, "wall_slide", 0, shooting=False)

    # -------------------------------------------------------------
    # INIMIGOS
    # -------------------------------------------------------------
    def _build_enemy_sprites(self):
        # 1. Metool (O robozinho de capacete icônico)
        # Hiding (escondido sob o capacete impenetrável)
        w, h = 24, 22
        s_hide = create_pixel_surface(w, h)
        # Capacete amarelo de segurança com símbolo verde
        pygame.draw.ellipse(s_hide, COLOR_ENEMY_YELLOW, (1, 3, 22, 17))
        pygame.draw.rect(s_hide, (210, 160, 20), (2, 14, 20, 5))
        # Cruz verde clássica no topo
        pygame.draw.rect(s_hide, (40, 200, 70), (10, 5, 4, 8))
        pygame.draw.rect(s_hide, (40, 200, 70), (8, 7, 8, 4))
        self.enemy_sprites["metool_hide"] = s_hide

        # Walk/Active (com olhos espiando e pezinhos)
        s_walk = create_pixel_surface(w, h)
        # Pés azuis
        pygame.draw.rect(s_walk, COLOR_X_BLUE, (3, 17, 6, 4))
        pygame.draw.rect(s_walk, COLOR_X_BLUE, (15, 17, 6, 4))
        # Rosto escuro com olhos
        pygame.draw.rect(s_walk, COLOR_BLACK, (4, 9, 16, 8))
        pygame.draw.rect(s_walk, COLOR_WHITE, (6, 11, 3, 4))
        pygame.draw.rect(s_walk, COLOR_WHITE, (14, 11, 3, 4))
        # Capacete levantado
        pygame.draw.ellipse(s_walk, COLOR_ENEMY_YELLOW, (1, 1, 22, 14))
        pygame.draw.rect(s_walk, (40, 200, 70), (10, 2, 4, 6))
        pygame.draw.rect(s_walk, (40, 200, 70), (8, 4, 8, 3))
        self.enemy_sprites["metool_walk"] = s_walk

        # 2. Batton (Morcego mecânico)
        bw, bh = 24, 24
        # Fechado (hanging)
        s_bat_hang = create_pixel_surface(bw, bh)
        pygame.draw.polygon(s_bat_hang, (70, 75, 105), [(12, 22), (2, 4), (22, 4)])
        pygame.draw.polygon(s_bat_hang, (110, 115, 150), [(12, 18), (5, 6), (19, 6)])
        pygame.draw.rect(s_bat_hang, (40, 45, 60), (10, 1, 4, 4)) # Garras no teto
        self.enemy_sprites["batton_hang"] = s_bat_hang

        # Aberto voando (flying)
        s_bat_fly1 = create_pixel_surface(bw, bh)
        pygame.draw.rect(s_bat_fly1, (70, 75, 105), (7, 6, 10, 10)) # Corpo
        pygame.draw.polygon(s_bat_fly1, (130, 60, 160), [(7, 8), (0, 2), (0, 12)]) # Asa esq
        pygame.draw.polygon(s_bat_fly1, (130, 60, 160), [(17, 8), (24, 2), (24, 12)]) # Asa dir
        pygame.draw.circle(s_bat_fly1, (255, 30, 50), (12, 11), 3) # Olho vermelho sensor
        self.enemy_sprites["batton_fly1"] = s_bat_fly1

        s_bat_fly2 = create_pixel_surface(bw, bh)
        pygame.draw.rect(s_bat_fly2, (70, 75, 105), (7, 6, 10, 10))
        pygame.draw.polygon(s_bat_fly2, (130, 60, 160), [(7, 10), (0, 16), (0, 6)])
        pygame.draw.polygon(s_bat_fly2, (130, 60, 160), [(17, 10), (24, 16), (24, 6)])
        pygame.draw.circle(s_bat_fly2, (255, 30, 50), (12, 11), 3)
        self.enemy_sprites["batton_fly2"] = s_bat_fly2

        # 3. Gunner Turret (Torreta)
        tw, th = 24, 24
        s_turret = create_pixel_surface(tw, th)
        pygame.draw.rect(s_turret, (50, 60, 80), (2, 12, 20, 10))
        pygame.draw.circle(s_turret, (100, 120, 150), (12, 12), 8)
        pygame.draw.rect(s_turret, (20, 25, 35), (4, 10, 16, 4))
        pygame.draw.circle(s_turret, (255, 60, 60), (12, 12), 3)
        self.enemy_sprites["turret"] = s_turret

        # 4. CHEFE: "Maverick Rex / Vile Bot"
        boss_w, boss_h = 44, 52
        s_boss = create_pixel_surface(boss_w, boss_h)
        # Armadura roxa metálica e dourada
        # Pernas robustas
        pygame.draw.rect(s_boss, COLOR_BOSS_PURPLE, (6, 32, 12, 18))
        pygame.draw.rect(s_boss, COLOR_BOSS_PURPLE, (26, 32, 12, 18))
        pygame.draw.rect(s_boss, COLOR_BOSS_GOLD, (4, 44, 14, 6))
        pygame.draw.rect(s_boss, COLOR_BOSS_GOLD, (26, 44, 14, 6))

        # Tronco reforçado
        pygame.draw.rect(s_boss, (40, 45, 60), (10, 16, 24, 18))
        pygame.draw.rect(s_boss, COLOR_BOSS_PURPLE, (12, 18, 20, 14))
        pygame.draw.rect(s_boss, COLOR_BOSS_GOLD, (16, 20, 12, 8))

        # Ombros com canhões
        pygame.draw.rect(s_boss, COLOR_BOSS_STEEL, (2, 12, 10, 10))
        pygame.draw.rect(s_boss, COLOR_BOSS_STEEL, (32, 12, 10, 10))

        # Cabeça / Elmo
        pygame.draw.rect(s_boss, COLOR_BOSS_PURPLE, (14, 4, 16, 14))
        pygame.draw.polygon(s_boss, COLOR_BOSS_GOLD, [(12, 4), (16, 0), (20, 4)])
        pygame.draw.polygon(s_boss, COLOR_BOSS_GOLD, [(24, 4), (28, 0), (32, 4)])
        # Visor vermelho ameaçador
        pygame.draw.rect(s_boss, (255, 30, 30), (16, 9, 12, 3))
        pygame.draw.rect(s_boss, COLOR_WHITE, (20, 9, 3, 2))

        self.enemy_sprites["boss_idle"] = s_boss

        # Chefe disparando / canhão ativado
        s_boss_atk = s_boss.copy()
        pygame.draw.rect(s_boss_atk, (255, 220, 50), (38, 14, 6, 6))
        self.enemy_sprites["boss_attack"] = s_boss_atk

    # -------------------------------------------------------------
    # PROJÉTEIS
    # -------------------------------------------------------------
    def _build_bullet_sprites(self):
        # 1. Buster Normal (Lemon shot)
        s1 = create_pixel_surface(10, 6)
        pygame.draw.ellipse(s1, COLOR_BUSTER_NORMAL, (0, 0, 10, 6))
        pygame.draw.ellipse(s1, COLOR_WHITE, (2, 1, 6, 4))
        self.bullet_sprites["normal"] = s1

        # 2. Charge Nível 1 (Esfera verde média)
        s2 = create_pixel_surface(16, 12)
        pygame.draw.ellipse(s2, COLOR_BUSTER_CHARGE_1, (0, 0, 16, 12))
        pygame.draw.ellipse(s2, (180, 255, 180), (3, 2, 10, 8))
        pygame.draw.ellipse(s2, COLOR_WHITE, (6, 3, 5, 5))
        self.bullet_sprites["charge_1"] = s2

        # 3. Charge Nível 2 (Mega Blast Espiral)
        s3 = create_pixel_surface(28, 20)
        # Halo de energia rosa/magenta
        pygame.draw.ellipse(s3, COLOR_BUSTER_CHARGE_PINK, (0, 0, 28, 20))
        # Núcleo de plasma ciano
        pygame.draw.ellipse(s3, COLOR_BUSTER_CHARGE_2, (3, 2, 22, 16))
        # Centro branco superaquecido
        pygame.draw.ellipse(s3, COLOR_WHITE, (7, 5, 14, 10))
        self.bullet_sprites["charge_2"] = s3

        # 4. Projétil do Inimigo
        se = create_pixel_surface(8, 8)
        pygame.draw.circle(se, COLOR_ENEMY_RED, (4, 4), 4)
        pygame.draw.circle(se, (255, 180, 50), (4, 4), 2)
        self.bullet_sprites["enemy"] = se

        # 5. Projétil do Chefe (Mega Plasma)
        sb = create_pixel_surface(18, 14)
        pygame.draw.ellipse(sb, COLOR_BOSS_PURPLE, (0, 0, 18, 14))
        pygame.draw.ellipse(sb, (255, 80, 120), (2, 2, 14, 10))
        pygame.draw.ellipse(sb, COLOR_WHITE, (5, 4, 8, 6))
        self.bullet_sprites["boss"] = sb

    # -------------------------------------------------------------
    # TILES E ELEMENTOS DO CENÁRIO
    # -------------------------------------------------------------
    def _build_tile_sprites(self):
        sz = TILE_SIZE

        # 1. Bloco de Chão de Metal com Beirada Luminosa
        s_floor = create_pixel_surface(sz, sz)
        pygame.draw.rect(s_floor, COLOR_TILE_METAL, (0, 0, sz, sz))
        pygame.draw.rect(s_floor, COLOR_TILE_TOP, (0, 0, sz, 4))
        pygame.draw.rect(s_floor, COLOR_TILE_ACCENT, (0, 4, sz, 1))
        # Parafusos industriais nos cantos
        for bx, by in [(3, 7), (sz - 5, 7), (3, sz - 5), (sz - 5, sz - 5)]:
            pygame.draw.rect(s_floor, (40, 50, 65), (bx, by, 2, 2))
        self.tile_sprites["floor"] = s_floor

        # 2. Bloco de Parede Metálica (ideal para Wall Slide)
        s_wall = create_pixel_surface(sz, sz)
        pygame.draw.rect(s_wall, (55, 65, 85), (0, 0, sz, sz))
        pygame.draw.rect(s_wall, (75, 90, 115), (1, 1, sz - 2, sz - 2))
        # Frisos verticais antiderrapantes
        pygame.draw.line(s_wall, (40, 50, 70), (8, 2), (8, sz - 2), 2)
        pygame.draw.line(s_wall, (40, 50, 70), (16, 2), (16, sz - 2), 2)
        pygame.draw.line(s_wall, (40, 50, 70), (24, 2), (24, sz - 2), 2)
        self.tile_sprites["wall"] = s_wall

        # 3. Plataforma Metálica Fina Flutuante
        s_plat = create_pixel_surface(sz, sz)
        pygame.draw.rect(s_plat, COLOR_TILE_TOP, (0, 0, sz, 8))
        pygame.draw.rect(s_plat, COLOR_TILE_ACCENT, (2, 2, sz - 4, 2))
        pygame.draw.rect(s_plat, (40, 50, 65), (0, 8, sz, 2))
        self.tile_sprites["platform"] = s_plat

        # 4. Espinhos (Spikes - Perigo mortal)
        s_spike = create_pixel_surface(sz, sz)
        # 3 dentes triangulares afiados
        pygame.draw.polygon(s_spike, (210, 40, 40), [(0, sz), (5, 4), (10, sz)])
        pygame.draw.polygon(s_spike, (210, 40, 40), [(11, sz), (16, 4), (21, sz)])
        pygame.draw.polygon(s_spike, (210, 40, 40), [(22, sz), (27, 4), (32, sz)])
        # Pontas afiadas brancas
        pygame.draw.line(s_spike, COLOR_WHITE, (5, 4), (5, 8), 1)
        pygame.draw.line(s_spike, COLOR_WHITE, (16, 4), (16, 8), 1)
        pygame.draw.line(s_spike, COLOR_WHITE, (27, 4), (27, 8), 1)
        self.tile_sprites["spikes"] = s_spike

        # 5. Portão do Chefe (Boss Shutter Door)
        s_door = create_pixel_surface(sz, sz)
        pygame.draw.rect(s_door, (30, 35, 45), (0, 0, sz, sz))
        pygame.draw.rect(s_door, (200, 160, 20), (2, 2, sz - 4, sz - 4))
        pygame.draw.rect(s_door, (240, 40, 40), (sz // 2 - 2, 4, 4, sz - 8))
        self.tile_sprites["door"] = s_door

    # -------------------------------------------------------------
    # ITENS COLETÁVEIS (RECARGA DE VIDA)
    # -------------------------------------------------------------
    def _build_item_sprites(self):
        # Cápsula Pequena de Vida
        s_sm = create_pixel_surface(12, 12)
        pygame.draw.circle(s_sm, (50, 220, 80), (6, 6), 5)
        pygame.draw.circle(s_sm, COLOR_WHITE, (6, 6), 3)
        pygame.draw.rect(s_sm, (20, 140, 40), (5, 2, 2, 8))
        self.item_sprites["health_small"] = s_sm

        # Cápsula Grande de Vida
        s_lg = create_pixel_surface(18, 18)
        pygame.draw.circle(s_lg, (50, 240, 90), (9, 9), 8)
        pygame.draw.circle(s_lg, COLOR_WHITE, (9, 9), 5)
        pygame.draw.circle(s_lg, (20, 180, 50), (9, 9), 3)
        self.item_sprites["health_large"] = s_lg
