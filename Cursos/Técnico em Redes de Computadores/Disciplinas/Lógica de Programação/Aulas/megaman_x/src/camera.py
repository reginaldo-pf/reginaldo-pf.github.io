"""
camera.py - Câmera 2D com rolagem suave (Lerp) e efeito de tremor (Screen Shake).
Mantém o foco no jogador respeitando as bordas do mapa da fase.
"""

import random
from .settings import INTERNAL_WIDTH, INTERNAL_HEIGHT

class Camera:
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.x = 0.0
        self.y = 0.0
        self.target_x = 0.0
        self.target_y = 0.0

        # Efeito de tremor de tela
        self.shake_time = 0.0
        self.shake_intensity = 0.0
        self.shake_offset_x = 0.0
        self.shake_offset_y = 0.0

    def update(self, target_rect, dt):
        # Centraliza o alvo com uma pequena antecipação horizontal
        target_center_x = target_rect.centerx - INTERNAL_WIDTH / 2
        target_center_y = target_rect.centery - INTERNAL_HEIGHT / 2 - 16

        # Interpolação linear suave (Lerp)
        lerp_factor = min(1.0, 8.0 * dt)
        self.x += (target_center_x - self.x) * lerp_factor
        self.y += (target_center_y - self.y) * lerp_factor

        # Limita a câmera dentro dos limites do mapa
        max_x = max(0, self.map_width - INTERNAL_WIDTH)
        max_y = max(0, self.map_height - INTERNAL_HEIGHT)
        self.x = max(0.0, min(self.x, float(max_x)))
        self.y = max(0.0, min(self.y, float(max_y)))

        # Atualiza tremor de tela (Screen Shake)
        if self.shake_time > 0:
            self.shake_time -= dt
            self.shake_offset_x = random.uniform(-self.shake_intensity, self.shake_intensity)
            self.shake_offset_y = random.uniform(-self.shake_intensity, self.shake_intensity)
        else:
            self.shake_offset_x = 0.0
            self.shake_offset_y = 0.0

    def add_shake(self, duration, intensity):
        self.shake_time = max(self.shake_time, duration)
        self.shake_intensity = max(self.shake_intensity, intensity)

    def get_offset(self):
        return (int(self.x + self.shake_offset_x), int(self.y + self.shake_offset_y))

    def apply_rect(self, rect):
        ox, oy = self.get_offset()
        return rect.move(-ox, -oy)
