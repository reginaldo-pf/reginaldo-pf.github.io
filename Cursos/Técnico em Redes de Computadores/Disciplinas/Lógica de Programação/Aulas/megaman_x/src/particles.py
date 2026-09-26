"""
particles.py - Sistema de efeitos visuais e partículas.
Responsável por poeira de dash, faíscas de wall slide, aura de carga do Buster,
fantasmas de movimento (afterimage) e explosões.
"""

import math
import random
import pygame
from .settings import (
    COLOR_WHITE, COLOR_X_CYAN, COLOR_BUSTER_CHARGE_1,
    COLOR_BUSTER_CHARGE_2, COLOR_BUSTER_CHARGE_PINK,
    COLOR_BUSTER_NORMAL, COLOR_ENEMY_RED
)

class Particle:
    def __init__(self, x, y, vx, vy, color, size, life, shrink=True, gravity=0.0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size
        self.initial_size = size
        self.life = life
        self.max_life = life
        self.shrink = shrink
        self.gravity = gravity

    def update(self, dt):
        self.life -= dt
        self.vy += self.gravity * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        if self.shrink and self.max_life > 0:
            ratio = max(0.0, self.life / self.max_life)
            self.size = max(1.0, self.initial_size * ratio)
        return self.life > 0

    def draw(self, surface, camera_offset):
        px = int(self.x - camera_offset[0])
        py = int(self.y - camera_offset[1])
        sz = int(self.size)
        if sz <= 1:
            surface.set_at((px, py), self.color)
        else:
            pygame.draw.circle(surface, self.color, (px, py), sz)

class GhostTrail:
    """Rastro translúcido deixado pelo jogador durante o Dash (efeito clássico)."""
    def __init__(self, surface, x, y, facing_right, life=0.15):
        self.surface = surface.copy()
        self.x = x
        self.y = y
        self.facing_right = facing_right
        self.life = life
        self.max_life = life
        # Tintura ciano translúcida
        tint = pygame.Surface(self.surface.get_size(), pygame.SRCALPHA)
        tint.fill((0, 200, 255, 120))
        self.surface.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def update(self, dt):
        self.life -= dt
        return self.life > 0

    def draw(self, target_surface, camera_offset):
        alpha = int(255 * (self.life / self.max_life))
        self.surface.set_alpha(alpha)
        px = int(self.x - camera_offset[0])
        py = int(self.y - camera_offset[1])
        target_surface.blit(self.surface, (px, py))

class ParticleSystem:
    def __init__(self):
        self.particles = []
        self.ghosts = []

    def clear(self):
        self.particles.clear()
        self.ghosts.clear()

    def add_dash_dust(self, x, y, direction):
        for _ in range(4):
            vx = -direction * random.uniform(30, 90) + random.uniform(-15, 15)
            vy = random.uniform(-25, -5)
            c = random.choice([(230, 235, 245), (180, 195, 210), (140, 150, 165)])
            self.particles.append(Particle(x, y, vx, vy, c, size=random.uniform(3, 5), life=0.25, shrink=True))

    def add_wall_slide_sparks(self, x, y, wall_direction):
        for _ in range(2):
            vx = -wall_direction * random.uniform(20, 60)
            vy = random.uniform(-40, 10)
            c = random.choice([(255, 240, 90), (255, 180, 30), (255, 255, 255)])
            self.particles.append(Particle(x, y, vx, vy, c, size=random.uniform(2, 3), life=0.18, shrink=True, gravity=200))

    def add_charge_particles(self, player_center, charge_level):
        """Partículas que orbitam e entram no X enquanto carrega o Buster."""
        color = COLOR_BUSTER_CHARGE_1 if charge_level == 1 else COLOR_BUSTER_CHARGE_PINK
        count = 2 if charge_level == 1 else 4
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            dist = random.uniform(18, 30)
            px = player_center[0] + math.cos(angle) * dist
            py = player_center[1] + math.sin(angle) * dist
            vx = -math.cos(angle) * 70
            vy = -math.sin(angle) * 70
            self.particles.append(Particle(px, py, vx, vy, color, size=2.5, life=0.22, shrink=True))

    def add_bullet_hit(self, x, y, color=COLOR_BUSTER_NORMAL):
        for _ in range(6):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(40, 110)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            self.particles.append(Particle(x, y, vx, vy, color, size=random.uniform(2, 4), life=0.20, shrink=True))

    def add_explosion(self, x, y, radius=18, count=24):
        colors = [(255, 255, 255), (255, 220, 50), (255, 120, 30), (230, 40, 40)]
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(30, 180)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            c = random.choice(colors)
            self.particles.append(Particle(x, y, vx, vy, c, size=random.uniform(3, 6), life=random.uniform(0.3, 0.5), shrink=True, gravity=90))

    def add_ghost(self, surface, x, y, facing_right):
        self.ghosts.append(GhostTrail(surface, x, y, facing_right))

    def update(self, dt):
        self.particles = [p for p in self.particles if p.update(dt)]
        self.ghosts = [g for g in self.ghosts if g.update(dt)]

    def draw(self, surface, camera_offset):
        for g in self.ghosts:
            g.draw(surface, camera_offset)
        for p in self.particles:
            p.draw(surface, camera_offset)
