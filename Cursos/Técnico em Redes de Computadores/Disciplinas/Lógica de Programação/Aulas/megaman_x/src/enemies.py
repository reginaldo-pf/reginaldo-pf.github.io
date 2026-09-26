"""
enemies.py - Inimigos clássicos (Metool, Batton, Gunner) e o Chefe Maverick.
Implementa máquinas de estados para comportamento dos inimigos,
inteligência artificial, armaduras dinâmicas e padrões de chefe.
"""

import math
import random
import pygame
from .settings import (
    COLOR_WHITE, COLOR_ENEMY_YELLOW, COLOR_BOSS_PURPLE
)
from .sprites import SpriteFactory
from .audio import SoundManager
from .bullet import EnemyBullet, BossBullet

class Pickup(pygame.sprite.Sprite):
    """Cápsula de recuperação de energia deixada por inimigos."""
    def __init__(self, x, y, is_large=False):
        super().__init__()
        self.x = float(x)
        self.y = float(y)
        self.vy = -120.0
        self.is_large = is_large
        self.amount = 8 if is_large else 3
        self.lifetime = 6.0

        sprites = SpriteFactory.get().item_sprites
        self.image = sprites["health_large"] if is_large else sprites["health_small"]
        self.rect = self.image.get_rect(center=(int(x), int(y)))

    def update(self, dt, tiles):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
            return

        # Queda suave com gravidade
        self.vy = min(self.vy + 400.0 * dt, 200.0)
        self.y += self.vy * dt
        self.rect.centery = int(self.y)

        # Colisão com o solo
        for tile in tiles:
            if tile.solid and self.rect.colliderect(tile.rect):
                if self.vy > 0:
                    self.rect.bottom = tile.rect.top
                    self.y = self.rect.y
                    self.vy = 0.0

    def draw(self, surface, camera_offset):
        # Pisca nos últimos 1.5 segundos
        if self.lifetime < 1.5 and int(self.lifetime * 10) % 2 == 0:
            return
        px = self.rect.x - camera_offset[0]
        py = self.rect.y - camera_offset[1]
        surface.blit(self.image, (px, py))

class Enemy(pygame.sprite.Sprite):
    """Classe base para todos os inimigos do jogo."""
    def __init__(self, x, y, hp, damage):
        super().__init__()
        self.x = float(x)
        self.y = float(y)
        self.vx = 0.0
        self.vy = 0.0
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.alive = True
        self.flash_timer = 0.0
        self.armored = False

        self.audio = SoundManager.get()
        self.sprites = SpriteFactory.get().enemy_sprites
        self.rect = pygame.Rect(int(x), int(y), 24, 24)

    def take_damage(self, amount, is_charge_shot=False, particle_system=None):
        """Aplica dano. Se estiver blindado, apenas tiros de carga máxima causam dano."""
        if self.armored and not is_charge_shot:
            self.audio.play('enemy_hit')
            if particle_system:
                particle_system.add_bullet_hit(self.rect.centerx, self.rect.centery, (255, 255, 100))
            return False

        self.hp -= amount
        self.flash_timer = 0.12
        self.audio.play('enemy_hit')

        if particle_system:
            particle_system.add_bullet_hit(self.rect.centerx, self.rect.centery, (255, 200, 50))

        if self.hp <= 0:
            self.alive = False
            self.audio.play('explosion')
            if particle_system:
                particle_system.add_explosion(self.rect.centerx, self.rect.centery, radius=20, count=20)
            self.kill()
        return True

    def update(self, dt, player, tiles, enemy_bullets, particle_system):
        if self.flash_timer > 0:
            self.flash_timer -= dt

    def draw(self, surface, camera_offset):
        px = self.rect.x - camera_offset[0]
        py = self.rect.y - camera_offset[1]

        # Efeito de silhueta branca ao levar dano (Hit Flash)
        if self.flash_timer > 0:
            white_surf = self.image.copy()
            white_surf.fill(COLOR_WHITE, special_flags=pygame.BLEND_RGB_MAX)
            surface.blit(white_surf, (px, py))
        else:
            surface.blit(self.image, (px, py))

# -------------------------------------------------------------
# 1. METOOL (O icônico robozinho de capacete)
# -------------------------------------------------------------
class Metool(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, hp=3, damage=2)
        self.image = self.sprites["metool_hide"]
        self.rect = pygame.Rect(int(x), int(y), 22, 20)
        self.state = "hiding"
        self.timer = 1.8
        self.facing_left = True
        self.armored = True

    def update(self, dt, player, tiles, enemy_bullets, particle_system):
        super().update(dt, player, tiles, enemy_bullets, particle_system)
        self.timer -= dt

        # Vira na direção do jogador
        self.facing_left = (player.rect.centerx < self.rect.centerx)

        if self.state == "hiding":
            self.armored = True
            self.image = self.sprites["metool_hide"]
            # Fica escondido por um tempo e depois levanta se o jogador estiver por perto
            dist = abs(player.rect.centerx - self.rect.centerx)
            if self.timer <= 0 and dist < 280:
                self.state = "peeking"
                self.timer = 0.5
                self.armored = False

        elif self.state == "peeking":
            self.armored = False
            self.image = self.sprites["metool_walk"]
            if self.timer <= 0:
                # Dispara 3 projéteis em leque
                self._shoot(enemy_bullets)
                self.state = "walking"
                self.timer = 1.0

        elif self.state == "walking":
            self.armored = False
            self.image = self.sprites["metool_walk"]
            # Anda devagar na direção do jogador
            spd = -35.0 if self.facing_left else 35.0
            self.x += spd * dt
            self.rect.x = int(self.x)

            if self.timer <= 0:
                self.state = "hiding"
                self.timer = 2.0

        if not self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

    def _shoot(self, enemy_bullets):
        bx = self.rect.centerx
        by = self.rect.centery - 2
        dir_x = -1.0 if self.facing_left else 1.0

        # Disparo triplo: reto, diagonal superior e diagonal inferior
        enemy_bullets.append(EnemyBullet(bx, by, dir_x * 190.0, 0.0))
        enemy_bullets.append(EnemyBullet(bx, by, dir_x * 170.0, -90.0))
        enemy_bullets.append(EnemyBullet(bx, by, dir_x * 170.0, 90.0))

# -------------------------------------------------------------
# 2. BATTON (Morcego Mecânico)
# -------------------------------------------------------------
class Batton(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, hp=2, damage=2)
        self.image = self.sprites["batton_hang"]
        self.rect = pygame.Rect(int(x), int(y), 22, 22)
        self.state = "hanging"
        self.armored = True
        self.origin_y = float(y)
        self.fly_timer = 0.0

    def update(self, dt, player, tiles, enemy_bullets, particle_system):
        super().update(dt, player, tiles, enemy_bullets, particle_system)

        dist_x = abs(player.rect.centerx - self.rect.centerx)
        dist_y = abs(player.rect.centery - self.rect.centery)

        if self.state == "hanging":
            self.armored = True
            self.image = self.sprites["batton_hang"]
            # Acorda quando o jogador se aproxima
            if dist_x < 180 and dist_y < 160:
                self.state = "flying"
                self.armored = False

        elif self.state == "flying":
            self.armored = False
            self.fly_timer += dt
            # Bate as asas
            self.image = self.sprites["batton_fly1"] if int(self.fly_timer * 8) % 2 == 0 else self.sprites["batton_fly2"]

            # Voa em curva ondulatória na direção do jogador
            dir_x = 1.0 if player.rect.centerx > self.rect.centerx else -1.0
            self.vx = dir_x * 85.0
            self.vy = math.sin(self.fly_timer * 6.0) * 90.0

            self.x += self.vx * dt
            self.y += self.vy * dt
            self.rect.x = int(self.x)
            self.rect.centery = int(self.y)

# -------------------------------------------------------------
# 3. GUNNER TURRET (Canhão Sentinela)
# -------------------------------------------------------------
class GunnerTurret(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, hp=4, damage=2)
        self.image = self.sprites["turret"]
        self.rect = pygame.Rect(int(x), int(y), 24, 24)
        self.shoot_cooldown = 1.8
        self.timer = random.uniform(0.5, 1.5)

    def update(self, dt, player, tiles, enemy_bullets, particle_system):
        super().update(dt, player, tiles, enemy_bullets, particle_system)
        self.timer -= dt

        dist = abs(player.rect.centerx - self.rect.centerx)
        if self.timer <= 0 and dist < 320:
            self.timer = self.shoot_cooldown
            # Dispara projétil na direção do jogador
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            length = math.hypot(dx, dy)
            if length > 0:
                vx = (dx / length) * 210.0
                vy = (dy / length) * 210.0
                enemy_bullets.append(EnemyBullet(self.rect.centerx, self.rect.centery, vx, vy))

# -------------------------------------------------------------
# 4. CHEFE DA FASE: MAVERICK REX (Vile Robot)
# -------------------------------------------------------------
class MaverickBoss(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, hp=32, damage=3)
        self.max_hp = 32
        self.image = self.sprites["boss_idle"]
        self.rect = pygame.Rect(int(x), int(y), 36, 48)
        self.state = "intro"
        self.intro_timer = 2.0
        self.display_hp = 0  # Enche a barra de vida no estilo clássico!
        self.timer = 1.0
        self.facing_left = True
        self.on_ground = False
        self.death_timer = 2.5
        self.exploded_count = 0

    def update(self, dt, player, tiles, enemy_bullets, particle_system, camera):
        super().update(dt, player, tiles, enemy_bullets, particle_system)

        # Atualiza a barra de vida clássica na introdução
        if self.state == "intro":
            self.intro_timer -= dt
            if self.display_hp < self.max_hp and int(self.intro_timer * 30) % 2 == 0:
                self.display_hp += 1
                self.audio.play('wall_kick')

            if self.intro_timer <= 0:
                self.display_hp = self.max_hp
                self.state = "idle"
                self.timer = 0.8
            return

        if self.state == "dying":
            self.death_timer -= dt
            self.image = self.sprites["boss_idle"]
            # Múltiplas explosões sequenciais
            if int(self.death_timer * 10) % 3 == 0:
                ex = self.rect.x + random.randint(0, self.rect.width)
                ey = self.rect.y + random.randint(0, self.rect.height)
                particle_system.add_explosion(ex, ey, radius=16, count=14)
                self.audio.play('explosion')
                camera.add_shake(0.15, 3.0)

            if self.death_timer <= 0:
                self.alive = False
                self.audio.play('victory')
                self.kill()
            return

        self.display_hp = self.hp
        self.facing_left = (player.rect.centerx < self.rect.centerx)
        self.timer -= dt

        # Gravidade para o chefe
        self.vy = min(self.vy + 800.0 * dt, 500.0)

        # ---------------------------------------------------------
        # MÁQUINA DE ESTADOS DO CHEFE
        # ---------------------------------------------------------
        if self.state == "idle":
            self.image = self.sprites["boss_idle"]
            self.vx = 0.0
            if self.timer <= 0:
                # Escolhe o próximo ataque
                atk = random.choice(["dash_attack", "jump_stomp", "triple_plasma"])
                self.state = atk
                if atk == "dash_attack":
                    self.timer = 1.1
                    self.audio.play('dash')
                elif atk == "jump_stomp":
                    self.vy = -450.0
                    self.on_ground = False
                    self.audio.play('jump')
                    self.timer = 1.8
                elif atk == "triple_plasma":
                    self.timer = 1.2
                    self._shoot_plasma(enemy_bullets)

        elif self.state == "dash_attack":
            self.image = self.sprites["boss_attack"]
            dir_x = -1.0 if self.facing_left else 1.0
            self.vx = dir_x * 240.0
            particle_system.add_dash_dust(self.rect.centerx, self.rect.bottom, int(dir_x))
            if self.timer <= 0:
                self.state = "idle"
                self.timer = 0.7

        elif self.state == "jump_stomp":
            self.image = self.sprites["boss_attack"]
            # Move-se horizontalmente em direção ao jogador no ar
            dir_x = -1.0 if self.facing_left else 1.0
            self.vx = dir_x * 120.0

            # Quando toca o chão, treme a tela (Stomp!)
            if self.on_ground and self.timer < 1.4:
                camera.add_shake(0.3, 5.0)
                self.audio.play('explosion')
                particle_system.add_dash_dust(self.rect.centerx, self.rect.bottom, 1)
                particle_system.add_dash_dust(self.rect.centerx, self.rect.bottom, -1)
                self.state = "idle"
                self.timer = 0.9

        elif self.state == "triple_plasma":
            self.image = self.sprites["boss_attack"]
            self.vx = 0.0
            if self.timer <= 0:
                self.state = "idle"
                self.timer = 0.8

        # Física e Colisão
        self.x += self.vx * dt
        self.rect.x = int(self.x)
        for tile in tiles:
            if tile.solid and self.rect.colliderect(tile.rect):
                if self.vx > 0:
                    self.rect.right = tile.rect.left
                    self.x = self.rect.x
                    self.vx = 0
                elif self.vx < 0:
                    self.rect.left = tile.rect.right
                    self.x = self.rect.x
                    self.vx = 0

        self.y += self.vy * dt
        self.rect.y = int(self.y)
        self.on_ground = False
        for tile in tiles:
            if tile.solid and self.rect.colliderect(tile.rect):
                if self.vy > 0:
                    self.rect.bottom = tile.rect.top
                    self.y = self.rect.y
                    self.vy = 0.0
                    self.on_ground = True
                elif self.vy < 0:
                    self.rect.top = tile.rect.bottom
                    self.y = self.rect.y
                    self.vy = 0.0

        if not self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

    def _shoot_plasma(self, enemy_bullets):
        bx = self.rect.centerx + (-20 if self.facing_left else 20)
        by = self.rect.centery - 4
        dir_x = -1.0 if self.facing_left else 1.0

        self.audio.play('charge_2_shot')
        enemy_bullets.append(BossBullet(bx, by - 10, dir_x * 260.0, -40.0))
        enemy_bullets.append(BossBullet(bx, by, dir_x * 280.0, 0.0))
        enemy_bullets.append(BossBullet(bx, by + 10, dir_x * 260.0, 40.0))

    def take_damage(self, amount, is_charge_shot=False, particle_system=None):
        if self.state in ["intro", "dying"]:
            return False

        self.hp -= amount
        self.flash_timer = 0.14
        self.audio.play('enemy_hit')

        if particle_system:
            particle_system.add_bullet_hit(self.rect.centerx, self.rect.centery, (255, 100, 255))

        if self.hp <= 0:
            self.hp = 0
            self.state = "dying"
            self.death_timer = 2.5
            self.audio.play('boss_siren')
        return True
