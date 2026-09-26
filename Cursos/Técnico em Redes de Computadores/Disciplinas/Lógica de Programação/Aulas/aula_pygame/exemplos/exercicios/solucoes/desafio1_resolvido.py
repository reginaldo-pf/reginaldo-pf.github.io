"""
SOLUCAO - EXERCICIO PRATICO 01: Bola Quicante e Mudanca de Cor
"""

import pygame
import sys
import random

def cor_aleatoria():
    return (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))

def main():
    pygame.init()
    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Desafio 01 - Resolvido: Bola Quicante")
    relogio = pygame.time.Clock()

    raio = 25
    x = float(LARGURA // 2)
    y = float(ALTURA // 2)
    vel_x = 6.0
    vel_y = 4.5
    cor_bola = (255, 100, 100)

    fonte = pygame.font.SysFont("Arial", 16)

    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        # Atualizacao do movimento
        x += vel_x
        y += vel_y

        # Borda Horizontal (Esquerda / Direita)
        if x + raio >= LARGURA:
            x = LARGURA - raio
            vel_x = -vel_x
            cor_bola = cor_aleatoria()
        elif x - raio <= 0:
            x = raio
            vel_x = -vel_x
            cor_bola = cor_aleatoria()

        # Borda Vertical (Topo / Base)
        if y + raio >= ALTURA:
            y = ALTURA - raio
            vel_y = -vel_y
            cor_bola = cor_aleatoria()
        elif y - raio <= 0:
            y = raio
            vel_y = -vel_y
            cor_bola = cor_aleatoria()

        # Renderizacao
        tela.fill((20, 25, 35))
        pygame.draw.circle(tela, cor_bola, (int(x), int(y)), raio)
        pygame.draw.circle(tela, (255, 255, 255), (int(x), int(y)), raio, width=2)

        txt = fonte.render(f"Posicao: ({int(x)}, {int(y)}) | Velocidade: ({vel_x}, {vel_y})", True, (180, 190, 205))
        tela.blit(txt, (20, 20))

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
