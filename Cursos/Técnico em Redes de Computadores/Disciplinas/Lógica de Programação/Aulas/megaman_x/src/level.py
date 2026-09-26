"""
level.py - Construção do mapa da fase, colisão de tiles, perigos e itens.
Contém design com seções de corrida, escalada vertical com Wall Jump,
poços de espinhos para Dash Jump e arena do Chefe.
"""

import random
import pygame
from .settings import (
    TILE_SIZE, INTERNAL_WIDTH, INTERNAL_HEIGHT,
    COLOR_BG, COLOR_SPIKE
)
from .sprites import SpriteFactory
from .enemies import Metool, Batton, GunnerTurret, MaverickBoss, Pickup

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type, solid=True, is_spike=False, is_door=False):
        super().__init__()
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.solid = solid
        self.is_spike = is_spike
        self.is_door = is_door
        self.tile_type = tile_type

        sprites = SpriteFactory.get().tile_sprites
        if tile_type in sprites:
            self.image = sprites[tile_type]
        else:
            self.image = sprites["floor"]

    def draw(self, surface, camera_offset):
        px = self.rect.x - camera_offset[0]
        py = self.rect.y - camera_offset[1]
        # Desenha apenas se estiver visível na tela
        if -TILE_SIZE <= px <= INTERNAL_WIDTH and -TILE_SIZE <= py <= INTERNAL_HEIGHT:
            surface.blit(self.image, (px, py))

class Level:
    def __init__(self):
        self.tiles = []
        self.solid_tiles = []
        self.hazard_tiles = []
        self.enemies = []
        self.pickups = []
        self.enemy_bullets = []
        self.boss = None
        self.boss_arena_x = 2650
        self.boss_triggered = False

        self.player_start_x = 100
        self.player_start_y = 350
        self.width = 0
        self.height = 0

        self._build_level_layout()
        self._generate_parallax_bg()

    def _generate_parallax_bg(self):
        """Gera silhuetas de prédios futuristas para o fundo parallax (estilo Central Highway)."""
        self.bg_buildings = []
        # Camada distante (prédios escuros e altos)
        random.seed(42)  # Semente fixa para consistência
        bx = 0
        while bx < 4000:
            bw = random.randint(50, 110)
            bh = random.randint(140, 260)
            color = random.choice([(14, 20, 36), (18, 25, 45), (10, 15, 28)])
            self.bg_buildings.append({"x": bx, "w": bw, "h": bh, "color": color, "layer": 0.2})
            bx += bw + random.randint(10, 30)

        # Camada média (prédios com janelas azuis e cianas)
        bx = 0
        while bx < 4000:
            bw = random.randint(60, 130)
            bh = random.randint(80, 180)
            color = random.choice([(25, 35, 58), (30, 42, 70), (22, 30, 50)])
            self.bg_buildings.append({"x": bx, "w": bw, "h": bh, "color": color, "layer": 0.5})
            bx += bw + random.randint(20, 50)

    def _build_level_layout(self):
        """
        Mapa em matriz de caracteres ASCII:
        '#' = Bloco sólido
        '=' = Plataforma metálica
        '^' = Espinhos mortais
        'D' = Portão da câmara do chefe
        'M' = Metool
        'B' = Batton
        'T' = Gunner Turret
        'K' = Chefe Maverick
        'h' = Cápsula de vida pequena
        'H' = Cápsula de vida grande
        'X' = Início do Jogador
        """
        # Dimensões: 18 linhas de altura x 115 colunas de largura (~3680px)
        # Altura: 18 * 32 = 576px
        ascii_map = [
            "###################################################################################################################",
            "#                                                                                                                 #",
            "#                                          B                                                                      #",
            "#                                      #######                                                                    #",
            "#                 H                    #     #                                                                    #",
            "#               #####                  #     #                                                                    #",
            "#                                      #     #            T                                                       #",
            "#                                      #     #        #########                                                   #",
            "#                                      #     #                                                                    #",
            "#                                      #     #                                 D                                  #",
            "#                     M                #     #                      M          D             K                    #",
            "#                 #########            #     #                  #########      D                                  #",
            "#                                      #     #                                 D                                  #",
            "#      M                  M            #     #                                 D                                  #",
            "#  #########          #########        #     #       T        #####            D                                  #",
            "#                                      #     #    #####                        D                                  #",
            "#                                      #     #              ^^^^^^^^^          D                                  #",
            "###################################################################################################################"
        ]

        self.height = len(ascii_map) * TILE_SIZE
        self.width = len(ascii_map[0]) * TILE_SIZE

        for row_idx, row in enumerate(ascii_map):
            for col_idx, char in enumerate(row):
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE

                if char == '#':
                    t = Tile(x, y, "floor", solid=True)
                    self.tiles.append(t)
                    self.solid_tiles.append(t)
                elif char == '=':
                    t = Tile(x, y, "platform", solid=True)
                    self.tiles.append(t)
                    self.solid_tiles.append(t)
                elif char == '^':
                    t = Tile(x, y, "spikes", solid=False, is_spike=True)
                    self.tiles.append(t)
                    self.hazard_tiles.append(t)
                elif char == 'D':
                    t = Tile(x, y, "door", solid=True, is_door=True)
                    self.tiles.append(t)
                    self.solid_tiles.append(t)
                elif char == 'M':
                    self.enemies.append(Metool(x, y + 10))
                elif char == 'B':
                    self.enemies.append(Batton(x, y))
                elif char == 'T':
                    self.enemies.append(GunnerTurret(x, y + 8))
                elif char == 'K':
                    self.boss = MaverickBoss(x, y)
                    self.enemies.append(self.boss)
                elif char == 'h':
                    self.pickups.append(Pickup(x + 16, y + 16, is_large=False))
                elif char == 'H':
                    self.pickups.append(Pickup(x + 16, y + 16, is_large=True))

        # Posição inicial do jogador
        self.player_start_x = 120
        self.player_start_y = 440

    def update(self, dt, player, particle_system, camera):
        # 1. Checa proximidade da câmara do chefe
        if not self.boss_triggered and player.rect.centerx > self.boss_arena_x:
            self.boss_triggered = True
            if self.boss:
                self.boss.audio.play('boss_siren')

        # 2. Atualiza Inimigos
        for enemy in self.enemies:
            if enemy == self.boss:
                enemy.update(dt, player, self.solid_tiles, self.enemy_bullets, particle_system, camera)
            else:
                enemy.update(dt, player, self.solid_tiles, self.enemy_bullets, particle_system)

        # Remove inimigos derrotados e sorteia chance de drop de vida
        dead_enemies = [e for e in self.enemies if not e.alive]
        for e in dead_enemies:
            if e != self.boss and random.random() < 0.40:
                is_large = (random.random() < 0.25)
                self.pickups.append(Pickup(e.rect.centerx, e.rect.centery, is_large))
        self.enemies = [e for e in self.enemies if e.alive]

        # 3. Atualiza Projéteis Inimigos
        for b in self.enemy_bullets:
            b.update(dt, self.solid_tiles)
            # Colisão com o jogador
            if b.rect.colliderect(player.rect):
                if player.take_damage(b.damage, camera=camera):
                    b.kill()
                    particle_system.add_bullet_hit(b.rect.centerx, b.rect.centery)
        self.enemy_bullets = [b for b in self.enemy_bullets if b.alive]

        # 4. Colisão: Tiros do Jogador vs Inimigos
        for bullet in player.bullets:
            for enemy in self.enemies:
                if enemy.alive and bullet.rect.colliderect(enemy.rect):
                    is_lvl2 = (bullet.charge_level == 2)
                    hit_success = enemy.take_damage(bullet.damage, is_charge_shot=is_lvl2, particle_system=particle_system)
                    bullet.on_hit()
                    break

        # 5. Colisão: Jogador vs Inimigos (Dano por contato)
        for enemy in self.enemies:
            if enemy.alive and player.rect.colliderect(enemy.rect):
                kb_dir = 1 if player.rect.centerx > enemy.rect.centerx else -1
                player.take_damage(enemy.damage, knockback_dir=kb_dir, camera=camera)

        # 6. Colisão: Jogador vs Espinhos (Perigo grave)
        for spike in self.hazard_tiles:
            # Hitbox menor no espinho para evitar colisões injustas
            hazard_box = spike.rect.inflate(-6, -8)
            if player.rect.colliderect(hazard_box):
                player.take_damage(4, knockback_dir=0, camera=camera)

        # 7. Coleta de Cápsulas de Vida
        for p in self.pickups:
            p.update(dt, self.solid_tiles)
            if player.rect.colliderect(p.rect):
                player.heal(p.amount)
                p.kill()
        self.pickups = [p for p in self.pickups if p.lifetime > 0]

    def draw_background(self, surface, camera_offset):
        """Renderiza o fundo estrelado e prédios com efeito de rolagem paralaxe."""
        surface.fill(COLOR_BG)
        cam_x, cam_y = camera_offset

        for b in self.bg_buildings:
            px = int(b["x"] - cam_x * b["layer"])
            py = INTERNAL_HEIGHT - b["h"] - int(cam_y * 0.1)
            pygame.draw.rect(surface, b["color"], (px, py, b["w"], b["h"]))

            # Janelas iluminadas nos prédios da camada média
            if b["layer"] > 0.3:
                for wx in range(px + 6, px + b["w"] - 6, 12):
                    for wy in range(py + 8, py + b["h"] - 10, 18):
                        if (wx * wy) % 7 < 3:
                            pygame.draw.rect(surface, (0, 210, 240, 180), (wx, wy, 4, 6))

    def draw(self, surface, camera_offset):
        # 1. Tiles do cenário
        for tile in self.tiles:
            tile.draw(surface, camera_offset)

        # 2. Cápsulas de vida
        for p in self.pickups:
            p.draw(surface, camera_offset)

        # 3. Projéteis inimigos
        for b in self.enemy_bullets:
            b.draw(surface, camera_offset)

        # 4. Inimigos
        for enemy in self.enemies:
            enemy.draw(surface, camera_offset)
