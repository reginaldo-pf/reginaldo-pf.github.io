"""
EXERCICIO PRATICO 02: Esquiva de Obstaculos (Dodge)
Dificuldade: Intermediario

ENUNCIADO:
O jogador controla um retangulo azul na parte inferior da tela, movendo-se
apenas para a esquerda e para a direita.
Meteoros/obstaculos vermelhos caem continuamente do topo da tela em velocidades
e posicoes X aleatorias.

OBJETIVO:
1. Impedir o jogador de sair pelas laterais da tela (borda esquerda e direita).
2. Fazer os obstaculos cairem continuamente. Quando um obstaculo alcanca a base da tela,
   ele deve reaparecer no topo com nova coordenada X aleatoria!
3. Detectar se algum obstaculo colidiu com o jogador (usando colliderect).
   Se colidir, reduza 1 vida do jogador.
"""

import pygame
import sys
import random

def main():
    pygame.init()
    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Desafio 02: Esquiva de Meteoros")
    relogio = pygame.time.Clock()

    # Jogador
    tam_jogador = 50
    jogador = pygame.Rect(LARGURA // 2 - tam_jogador // 2, ALTURA - 70, tam_jogador, 40)
    vel_jogador = 7

    # Lista de obstaculos
    # Cada obstaculo e um Rect(x, y, largura, altura)
    obstaculos = []
    for _ in range(4):
        obs = pygame.Rect(random.randint(20, LARGURA - 50), random.randint(-400, -50), 35, 35)
        obstaculos.append(obs)

    vidas = 3
    pontos = 0
    fonte = pygame.font.SysFont("Arial", 22, bold=True)

    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        teclas = pygame.key.get_pressed()
        # Movimentacao horizontal
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            jogador.x -= vel_jogador
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jogador.x += vel_jogador

        # TODO 1: Limitar o jogador dentro da tela (jogador.left >= 0 e jogador.right <= LARGURA)

        # TODO 2: Fazer cada obstaculo cair (obs.y += velocidade)
        # Se obs.top > ALTURA:
        #    reposicionar no topo: obs.y = random.randint(-150, -40)
        #    e obs.x = random.randint(20, LARGURA - 50)
        #    somar +1 nos pontos

        # TODO 3: Verificar colisao com o jogador usando jogador.colliderect(obs)
        # Se colidir:
        #    reduzir vidas -= 1
        #    reposicionar o obstaculo no topo

        tela.fill((15, 18, 28))

        # Desenhar jogador
        pygame.draw.rect(tela, (60, 150, 255), jogador, border_radius=6)

        # Desenhar obstaculos
        for obs in obstaculos:
            pygame.draw.rect(tela, (255, 70, 70), obs, border_radius=4)

        # HUD
        txt_vidas = fonte.render(f"Vidas: {vidas}", True, (255, 100, 100))
        txt_pts = fonte.render(f"Pontos: {pontos}", True, (255, 215, 0))
        tela.blit(txt_vidas, (20, 20))
        tela.blit(txt_pts, (150, 20))

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
