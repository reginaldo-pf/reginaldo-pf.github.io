"""
main.py - Ponto de entrada do jogo Mega Man X.
Gerencia o loop principal, máquina de estados (Title, Playing, GameOver, Victory),
renderização interna escalada para alta definição e controle de taxa de quadros (60 FPS).
"""

import sys
import pygame
from src.settings import (
    INTERNAL_WIDTH, INTERNAL_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, FPS,
    KEY_START, KEY_PAUSE
)
from src.player import Player
from src.level import Level
from src.camera import Camera
from src.particles import ParticleSystem
from src.ui import UI
from src.audio import SoundManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Mega Man X - Projeto Final (Python)")

        # Cria a janela principal escalada
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # Superfície interna de baixa resolução (visuais retrô nítidos 16-bits)
        self.display_surface = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # Inicializa subsistemas
        self.audio = SoundManager.get()
        self.ui = UI()
        self.state = "TITLE"
        self.blink_timer = 0.0
        self.blink_state = True

        self.level = None
        self.player = None
        self.camera = None
        self.particle_system = None
        self.reset_game()

    def reset_game(self):
        """Reinicia o nível e o jogador do início."""
        self.level = Level()
        self.player = Player(self.level.player_start_x, self.level.player_start_y)
        self.camera = Camera(self.level.width, self.level.height)
        self.particle_system = ParticleSystem()

    def run(self):
        while self.running:
            # Delta time limitado a 0.05s para prevenir instabilidade física
            dt = min(self.clock.tick(FPS) / 1000.0, 0.05)
            self.blink_timer += dt
            if self.blink_timer >= 0.5:
                self.blink_timer = 0.0
                self.blink_state = not self.blink_state

            just_pressed = []
            just_released = []

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    just_pressed.append(event.key)
                    if event.key in KEY_PAUSE:
                        if self.state == "PLAYING":
                            pass # Pausa opcional
                elif event.type == pygame.KEYUP:
                    just_released.append(event.key)

            keys_pressed = pygame.key.get_pressed()

            # ---------------------------------------------------------
            # MÁQUINA DE ESTADOS DO JOGO
            # ---------------------------------------------------------
            if self.state == "TITLE":
                if any(k in just_pressed for k in KEY_START):
                    self.reset_game()
                    self.state = "PLAYING"
                self.ui.draw_title_screen(self.display_surface, self.blink_state)

            elif self.state == "PLAYING":
                self._update_playing(dt, keys_pressed, just_pressed, just_released)
                self._draw_playing()

            elif self.state == "GAME_OVER":
                if any(k in just_pressed for k in KEY_START):
                    self.reset_game()
                    self.state = "PLAYING"
                self._draw_playing()
                self.ui.draw_game_over(self.display_surface)

            elif self.state == "VICTORY":
                if any(k in just_pressed for k in KEY_START):
                    self.reset_game()
                    self.state = "TITLE"
                self._draw_playing()
                self.ui.draw_victory(self.display_surface)

            # Escala a superfície interna para o tamanho real da janela com interpolação nítida
            scaled_surf = pygame.transform.scale(self.display_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.window.blit(scaled_surf, (0, 0))
            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def _update_playing(self, dt, keys_pressed, just_pressed, just_released):
        # 1. Entrada do jogador
        self.player.handle_input(keys_pressed, just_pressed, just_released, self.camera)

        # 2. Atualização de física do jogador
        self.player.update(dt, self.level.solid_tiles, self.particle_system, self.camera)

        # 3. Atualização do nível e combate
        self.level.update(dt, self.player, self.particle_system, self.camera)

        # 4. Atualização de partículas
        self.particle_system.update(dt)

        # 5. Câmera acompanha o jogador
        self.camera.update(self.player.rect, dt)

        # 6. Condições de derrota e vitória
        if self.player.hp <= 0:
            self.state = "GAME_OVER"

        if self.level.boss and not self.level.boss.alive and self.level.boss.death_timer <= 0:
            self.state = "VICTORY"

    def _draw_playing(self):
        cam_offset = self.camera.get_offset()

        # 1. Fundo Paralaxe com prédios
        self.level.draw_background(self.display_surface, cam_offset)

        # 2. Cenário, perigos e inimigos
        self.level.draw(self.display_surface, cam_offset)

        # 3. Jogador
        self.player.draw(self.display_surface, cam_offset)

        # 4. Partículas e Efeitos Especiais
        self.particle_system.draw(self.display_surface, cam_offset)

        # 5. Interface HUD (Barras de Vida)
        self.ui.draw_hud(
            self.display_surface,
            self.player,
            self.level.boss,
            boss_active=self.level.boss_triggered
        )

if __name__ == "__main__":
    game = Game()
    game.run()
