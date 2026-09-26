"""
bullet.py - Projéteis do jogador e dos inimigos.
Suporta tiro simples (lemon), tiros carregados de níveis 1 e 2,
tiros de inimigos e projéteis especiais de chefes.
"""

import pygame
from .settings import (
    DAMAGE_BUSTER_NORMAL, DAMAGE_BUSTER_CHARGE_1, DAMAGE_BUSTER_CHARGE_2
)
from .sprites import SpriteFactory

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy, damage, is_player=True, piercing=False):
        super().__init__()
        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)
        self.damage = damage
        self.is_player = is_player
        self.piercing = piercing
        self.pierce_count = 3 if piercing else 1
        self.alive = True
        self.lifetime = 2.5  # Segundos antes de sumir se não acertar nada

        # Configurado na subclasse
        self.image = None
        self.rect = pygame.Rect(int(self.x), int(self.y), 8, 8)

    def update(self, dt, tiles):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
            return

        self.x += self.vx * dt
        self.y += self.vy * dt
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

        # Colisão com paredes sólidas do cenário
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                # Tiros simples e médios explodem na parede; tiro nível 2 também colide com parede sólida
                self.kill()
                return

    def on_hit(self):
        """Chamado quando o projétil atinge um alvo válido."""
        if not self.piercing:
            self.kill()
        else:
            self.pierce_count -= 1
            if self.pierce_count <= 0:
                self.kill()

    def draw(self, surface, camera_offset):
        px = self.rect.x - camera_offset[0]
        py = self.rect.y - camera_offset[1]
        surface.blit(self.image, (px, py))

class BusterBullet(Bullet):
    """Projétil disparado pelo Mega Man X (Buster)."""
    def __init__(self, x, y, direction, charge_level=0):
        sprites = SpriteFactory.get().bullet_sprites

        if charge_level == 2:
            img = sprites["charge_2"]
            speed = 520.0
            dmg = DAMAGE_BUSTER_CHARGE_2
            piercing = True
        elif charge_level == 1:
            img = sprites["charge_1"]
            speed = 460.0
            dmg = DAMAGE_BUSTER_CHARGE_1
            piercing = False
        else:
            img = sprites["normal"]
            speed = 420.0
            dmg = DAMAGE_BUSTER_NORMAL
            piercing = False

        # Inverte horizontalmente se atirar para a esquerda
        if direction < 0:
            img = pygame.transform.flip(img, True, False)

        super().__init__(x, y, speed * direction, 0, dmg, is_player=True, piercing=piercing)
        self.image = img
        self.charge_level = charge_level
        self.rect = self.image.get_rect(center=(int(x), int(y)))

class EnemyBullet(Bullet):
    """Projétil disparado por inimigos comuns."""
    def __init__(self, x, y, vx, vy, damage=2):
        super().__init__(x, y, vx, vy, damage=damage, is_player=False, piercing=False)
        self.image = SpriteFactory.get().bullet_sprites["enemy"]
        self.rect = self.image.get_rect(center=(int(x), int(y)))

class BossBullet(Bullet):
    """Projétil massivo do Chefe."""
    def __init__(self, x, y, vx, vy, damage=4):
        super().__init__(x, y, vx, vy, damage=damage, is_player=False, piercing=False)
        img = SpriteFactory.get().bullet_sprites["boss"]
        if vx < 0:
            img = pygame.transform.flip(img, True, False)
        self.image = img
        self.rect = self.image.get_rect(center=(int(x), int(y)))
