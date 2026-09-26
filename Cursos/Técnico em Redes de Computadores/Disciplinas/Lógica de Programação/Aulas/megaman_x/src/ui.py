"""
ui.py - Interface do Usuário (HUD), barras de energia clássicas e telas de transição.
Desenha as barras de vida verticais icônicas de Mega Man X, tela de título,
Game Over e Stage Clear.
"""

import pygame
from .settings import (
    INTERNAL_WIDTH, INTERNAL_HEIGHT, COLOR_WHITE, COLOR_BLACK,
    COLOR_X_CYAN, COLOR_X_BLUE, COLOR_BOSS_PURPLE, COLOR_BOSS_GOLD
)

class UI:
    def __init__(self):
        # Carrega fontes padrão com fallback seguro
        pygame.font.init()
        self.font_title = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 24)
        self.font_small = pygame.font.Font(None, 18)

    def draw_health_bar(self, surface, x, y, current_hp, max_hp, is_boss=False, label=""):
        """Desenha a barra vertical clássica de energia segmentada do Mega Man X."""
        bar_w = 8
        bar_h = max_hp * 3 + 6  # 3 pixels por segmento de vida + bordas
        outer_rect = pygame.Rect(x - 2, y - 2, bar_w + 4, bar_h + 4)

        # Moldura metálica externa
        pygame.draw.rect(surface, (20, 25, 35), outer_rect)
        pygame.draw.rect(surface, (90, 105, 130), outer_rect, 1)

        # Segmentos de energia
        c_fill = (240, 220, 50) if not is_boss else (220, 50, 100)
        c_core = COLOR_WHITE if not is_boss else (255, 180, 120)

        for i in range(max_hp):
            seg_y = y + bar_h - 4 - (i * 3)
            seg_rect = pygame.Rect(x, seg_y, bar_w, 2)
            if i < current_hp:
                pygame.draw.rect(surface, c_fill, seg_rect)
                surface.set_at((x + 1, seg_y), c_core)
            else:
                pygame.draw.rect(surface, (30, 35, 45), seg_rect)

        # Etiqueta (ex: 'X' ou 'BOSS')
        if label:
            txt = self.font_small.render(label, True, COLOR_WHITE)
            surface.blit(txt, (x - 2, y - 14))

    def draw_hud(self, surface, player, boss=None, boss_active=False):
        # 1. Barra de Vida do Mega Man X
        self.draw_health_bar(surface, 14, 28, player.hp, player.max_hp, is_boss=False, label="X")

        # 2. Indicador de Carga do Buster
        if player.charge_level > 0:
            c = (50, 255, 100) if player.charge_level == 1 else (0, 230, 255)
            txt = "CHARGE 1" if player.charge_level == 1 else "MAX CHARGE!"
            lbl = self.font_small.render(txt, True, c)
            surface.blit(lbl, (28, 28))

        # 3. Barra de Vida do Chefe
        if boss_active and boss and boss.alive:
            bx = INTERNAL_WIDTH - 22
            self.draw_health_bar(surface, bx, 28, boss.display_hp, boss.max_hp, is_boss=True, label="BOSS")

    def draw_title_screen(self, surface, blink_state):
        """Tela de Título Retro."""
        # Fundo sombreado
        surface.fill((12, 16, 26))

        # Logo / Título
        title_text = self.font_title.render("MEGA MAN X", True, COLOR_X_CYAN)
        sub_text = self.font_medium.render("PROJETO FINAL - PYTHON EDITION", True, COLOR_WHITE)

        surface.blit(title_text, (INTERNAL_WIDTH // 2 - title_text.get_width() // 2, 60))
        surface.blit(sub_text, (INTERNAL_WIDTH // 2 - sub_text.get_width() // 2, 98))

        # Painel de Controles
        ctrl_y = 150
        panel_w = 420
        panel_h = 130
        panel_rect = pygame.Rect(INTERNAL_WIDTH // 2 - panel_w // 2, ctrl_y, panel_w, panel_h)
        pygame.draw.rect(surface, (22, 28, 44), panel_rect)
        pygame.draw.rect(surface, COLOR_X_BLUE, panel_rect, 2)

        header = self.font_medium.render("COMANDOS DO JOGADOR:", True, (255, 220, 60))
        surface.blit(header, (panel_rect.x + 16, ctrl_y + 10))

        controls = [
            "Setas / A, D : Mover para os lados",
            "ESPAÇO / Z / K : Pular (Segure p/ Pular Alto, Quicar na parede)",
            "X / J : Disparar (Segure para Mega Buster Carregado)",
            "C / SHIFT / L : Dash (Investida veloz, tente Dash Jump!)",
        ]

        for idx, line in enumerate(controls):
            c_txt = self.font_small.render(line, True, (210, 225, 240))
            surface.blit(c_txt, (panel_rect.x + 16, ctrl_y + 38 + idx * 20))

        # Mensagem piscante "PRESS ENTER"
        if blink_state:
            start_txt = self.font_medium.render("PRESSIONE ENTER OU ESPAÇO PARA INICIAR", True, (0, 240, 210))
            surface.blit(start_txt, (INTERNAL_WIDTH // 2 - start_txt.get_width() // 2, 305))

    def draw_game_over(self, surface):
        """Tela de Game Over."""
        overlay = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT), pygame.SRCALPHA)
        overlay.fill((10, 10, 20, 200))
        surface.blit(overlay, (0, 0))

        t = self.font_title.render("MISSION FAILED", True, (240, 50, 50))
        sub = self.font_medium.render("O Maverick destruiu o X...", True, COLOR_WHITE)
        prompt = self.font_small.render("Pressione ENTER ou ESPAÇO para Tentar Novamente", True, (255, 220, 80))

        surface.blit(t, (INTERNAL_WIDTH // 2 - t.get_width() // 2, 110))
        surface.blit(sub, (INTERNAL_WIDTH // 2 - sub.get_width() // 2, 160))
        surface.blit(prompt, (INTERNAL_WIDTH // 2 - prompt.get_width() // 2, 220))

    def draw_victory(self, surface):
        """Tela de Vitória / Stage Clear."""
        overlay = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT), pygame.SRCALPHA)
        overlay.fill((8, 25, 40, 210))
        surface.blit(overlay, (0, 0))

        t = self.font_title.render("STAGE CLEAR!", True, (0, 255, 210))
        sub = self.font_medium.render("MAVERICK REX DESTRUIDO!", True, (255, 230, 80))
        msg = self.font_small.render("Parabéns! Missão cumprida com sucesso.", True, COLOR_WHITE)
        prompt = self.font_small.render("Pressione ENTER ou ESPAÇO para Jogar Novamente", True, (180, 240, 255))

        surface.blit(t, (INTERNAL_WIDTH // 2 - t.get_width() // 2, 100))
        surface.blit(sub, (INTERNAL_WIDTH // 2 - sub.get_width() // 2, 145))
        surface.blit(msg, (INTERNAL_WIDTH // 2 - msg.get_width() // 2, 185))
        surface.blit(prompt, (INTERNAL_WIDTH // 2 - prompt.get_width() // 2, 235))
