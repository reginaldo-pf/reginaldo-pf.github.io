"""
EXERCICIO PRATICO 01: Bola Quicante e Mudanca de Cor
Dificuldade: Facil / Introdutorio

ENUNCIADO:
Complete o codigo abaixo para fazer a bola rebater continuamente em todas as 4
bordas da janela (esquerda, direita, topo e base). Toda vez que a bola tocar em uma borda,
ela deve mudar para uma nova cor aleatoria!

DICAS:
- Inverter vel_x quando a bola atingir a borda esquerda (<= raio) ou direita (>= LARGURA - raio).
- Inverter vel_y quando atingir o topo (<= raio) ou base (>= ALTURA - raio).
- Use random.randint(50, 255) para sortear componentes R, G e B ao colidir.
"""

import pygame
import sys
import random

def main():
    pygame.init()
    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Desafio 01: Bola Quicante")
    relogio = pygame.time.Clock()

    # Variaveis da bolinha
    raio = 25
    x = LARGURA // 2
    y = ALTURA // 2
    vel_x = 5
    vel_y = 4
    cor_bola = (255, 100, 100)

    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        # TODO 1: Atualizar a posicao da bola com as velocidades
        # x += ...
        # y += ...

        # TODO 2: Detectar impacto nas bordas horizontais (X) e inverter vel_x
        # Se bater, troque cor_bola = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
        
        # TODO 3: Detectar impacto nas bordas verticais (Y) e inverter vel_y
        # Se bater, troque tambem a cor_bola

        tela.fill((20, 25, 35))

        # Desenha a bola
        pygame.draw.circle(tela, cor_bola, (int(x), int(y)), raio)

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
