"""
SOLUCAO - EXERCICIO PRATICO 02: Esquiva de Obstaculos (Dodge)
"""

import pygame
import sys
import random

def main():
    pygame.init()
    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Desafio 02 - Resolvido: Esquiva de Obstaculos")
    relogio = pygame.time.Clock()

    tam_jogador = 50
    jogador = pygame.Rect(LARGURA // 2 - tam_jogador // 2, ALTURA - 70, tam_jogador, 40)
    vel_jogador = 8

    # Cada elemento da lista contem: [rect, velocidade_queda]
    obstaculos = []
    for _ in range(5):
        rect = pygame.Rect(random.randint(20, LARGURA - 50), random.randint(-400, -50), 36, 36)
        vel = random.randint(4, 7)
        obstaculos.append([rect, vel])

    vidas = 3
    pontos = 0
    game_over = False

    fonte = pygame.font.SysFont("Arial", 22, bold=True)
    fonte_fim = pygame.font.SysFont("Arial", 42, bold=True)

    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.KEYDOWN and game_over:
                if evento.key == pygame.K_r:
                    # Reinicia
                    vidas = 3
                    pontos = 0
                    game_over = False
                    for item in obstaculos:
                        item[0].x = random.randint(20, LARGURA - 50)
                        item[0].y = random.randint(-400, -50)

        if not game_over:
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                jogador.x -= vel_jogador
            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                jogador.x += vel_jogador

            # 1. Limite de bordas
            if jogador.left < 0:
                jogador.left = 0
            if jogador.right > LARGURA:
                jogador.right = LARGURA

            # 2. Queda dos obstaculos e colisoes
            for item in obstaculos:
                obs_rect, obs_vel = item
                obs_rect.y += obs_vel

                # Se passou do final da tela
                if obs_rect.top > ALTURA:
                    obs_rect.y = random.randint(-200, -40)
                    obs_rect.x = random.randint(20, LARGURA - 50)
                    item[1] = random.randint(4, 8)
                    pontos += 1

                # 3. Colisao com jogador
                if jogador.colliderect(obs_rect):
                    vidas -= 1
                    obs_rect.y = random.randint(-250, -60)
                    obs_rect.x = random.randint(20, LARGURA - 50)
                    if vidas <= 0:
                        game_over = True

        # Renderizacao
        tela.fill((15, 18, 28))

        if not game_over:
            # Jogador
            pygame.draw.rect(tela, (60, 150, 255), jogador, border_radius=6)
            pygame.draw.circle(tela, (255, 255, 255), jogador.center, 6)

            # Obstaculos
            for item in obstaculos:
                obs = item[0]
                pygame.draw.rect(tela, (255, 75, 75), obs, border_radius=5)
                pygame.draw.circle(tela, (255, 180, 180), obs.center, 5)

            # HUD
            txt_vidas = fonte.render(f"Vidas: {vidas}", True, (255, 100, 100))
            txt_pts = fonte.render(f"Pontos: {pontos}", True, (255, 215, 0))
            tela.blit(txt_vidas, (20, 20))
            tela.blit(txt_pts, (150, 20))
        else:
            txt_fim = fonte_fim.render("FIM DE JOGO!", True, (255, 80, 80))
            txt_sub = fonte.render(f"Pontuacao: {pontos} | Pressione [ R ] para Reiniciar", True, (240, 240, 240))
            tela.blit(txt_fim, txt_fim.get_rect(center=(LARGURA // 2, ALTURA // 2 - 30)))
            tela.blit(txt_sub, txt_sub.get_rect(center=(LARGURA // 2, ALTURA // 2 + 30)))

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
