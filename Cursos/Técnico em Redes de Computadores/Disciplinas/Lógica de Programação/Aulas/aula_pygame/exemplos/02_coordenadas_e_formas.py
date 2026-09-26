"""
Aula 01: Introducao ao Pygame
Exemplo 02: Sistema de Coordenadas e Formas Geometricas (pygame.draw)

Conceitos abordados:
1. O plano cartesiano na computacao grafica 2D:
   - Origem (0, 0) no canto superior esquerdo (Top-Left)
   - X cresce para a DIREITA
   - Y cresce para BAIXO (diferente da matematica escolar!)
2. O sistema de cores RGB (Red, Green, Blue)
3. Desenhando primitivos graficos: rect, circle, line, polygon
4. Renderizando texto basico com as coordenadas do mouse em tempo real
"""

import pygame
import sys

def main():
    pygame.init()

    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Pygame - Exemplo 02: Coordenadas e Formas Geometricas")
    relogio = pygame.time.Clock()

    # --- PALETA DE CORES (R, G, B) de 0 a 255 ---
    COR_FUNDO  = (20, 24, 33)       # Fundo azul meia-noite escuro
    BRANCO     = (255, 255, 255)
    VERMELHO   = (235, 75, 75)
    VERDE      = (75, 215, 120)
    AZUL       = (60, 140, 240)
    AMARELO    = (255, 210, 60)
    MAGENTA    = (210, 80, 220)
    CINZA_EIXO = (60, 70, 90)

    # Fonte para escrever informacoes e rotulos na tela
    fonte = pygame.font.SysFont("Arial", 18, bold=True)
    fonte_pequena = pygame.font.SysFont("Arial", 14)

    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        # Obtem a posicao atual do cursor do mouse (x, y)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # 1. Limpa a tela
        tela.fill(COR_FUNDO)

        # 2. Desenha eixos e grade de referencia para fixar o conceito de coordenadas
        # Linha horizontal do topo (Eixo X) e Linha vertical esquerda (Eixo Y)
        pygame.draw.line(tela, CINZA_EIXO, (0, 0), (LARGURA, 0), 6)
        pygame.draw.line(tela, CINZA_EIXO, (0, 0), (0, ALTURA), 6)
        
        # Marcacao da Origem (0, 0)
        pygame.draw.circle(tela, AMARELO, (0, 0), 12)
        txt_origem = fonte_pequena.render("(0, 0) Origem", True, AMARELO)
        tela.blit(txt_origem, (15, 8))

        # Indicadores de direcao dos eixos
        txt_eixo_x = fonte_pequena.render("--> X aumenta para a Direita", True, BRANCO)
        tela.blit(txt_eixo_x, (200, 8))

        txt_eixo_y = fonte_pequena.render("| v Y aumenta para BAIXO", True, BRANCO)
        tela.blit(txt_eixo_y, (10, 40))

        # --- 3. DESENHO DE FORMAS GEOMETRICAS (pygame.draw) ---

        # [A] Retangulo preenchido: (x, y, largura, altura)
        # Posicao: X=80, Y=100 | Dimensoes: Largura=160, Altura=100
        pygame.draw.rect(tela, AZUL, (80, 100, 160, 100), border_radius=8)
        lbl1 = fonte_pequena.render("pygame.draw.rect", True, BRANCO)
        tela.blit(lbl1, (80, 210))

        # [B] Retangulo com apenas borda (espessura = 3)
        pygame.draw.rect(tela, VERDE, (280, 100, 160, 100), width=3, border_radius=8)
        lbl2 = fonte_pequena.render("rect (borda width=3)", True, BRANCO)
        tela.blit(lbl2, (280, 210))

        # [C] Circulo preenchido: (centro_x, centro_y), raio
        # Centro: X=560, Y=150 | Raio: 50 pixels
        pygame.draw.circle(tela, VERMELHO, (560, 150), 50)
        lbl3 = fonte_pequena.render("pygame.draw.circle", True, BRANCO)
        tela.blit(lbl3, (500, 210))

        # [D] Circulo vazado (apenas borda):
        pygame.draw.circle(tela, AMARELO, (700, 150), 40, width=4)
        lbl4 = fonte_pequena.render("circle (width=4)", True, BRANCO)
        tela.blit(lbl4, (650, 210))

        # [E] Linha reta diagonal: (x1, y1) ate (x2, y2)
        pygame.draw.line(tela, MAGENTA, (80, 280), (300, 360), width=5)
        lbl5 = fonte_pequena.render("pygame.draw.line", True, BRANCO)
        tela.blit(lbl5, (80, 370))

        # [F] Poligono (Triangulo desenhado por lista de vertices)
        pontos_triangulo = [(440, 370), (370, 280), (510, 280)]
        pygame.draw.polygon(tela, AMARELO, pontos_triangulo)
        lbl6 = fonte_pequena.render("pygame.draw.polygon", True, BRANCO)
        tela.blit(lbl6, (380, 380))

        # [G] Elipse / Oval inscrita em um retangulo
        pygame.draw.ellipse(tela, VERDE, (580, 280, 160, 90), width=3)
        lbl7 = fonte_pequena.render("pygame.draw.ellipse", True, BRANCO)
        tela.blit(lbl7, (600, 380))

        # --- 4. EXIBICAO DINAMICA DA POSICAO DO MOUSE ---
        # Desenha miras seguindo o mouse para o aluno testar qualquer posicao
        pygame.draw.circle(tela, BRANCO, (mouse_x, mouse_y), 6)
        pygame.draw.line(tela, (100, 100, 100), (mouse_x, 0), (mouse_x, ALTURA), 1)
        pygame.draw.line(tela, (100, 100, 100), (0, mouse_y), (LARGURA, mouse_y), 1)

        # Painel informativo inferior
        painel_rect = pygame.Rect(40, 480, 720, 90)
        pygame.draw.rect(tela, (35, 42, 58), painel_rect, border_radius=10)
        pygame.draw.rect(tela, AZUL, painel_rect, width=2, border_radius=10)

        info_mouse = fonte.render(f"Posicao do Cursor (Mouse): X = {mouse_x} | Y = {mouse_y}", True, AMARELO)
        info_dica = fonte_pequena.render("Mova o cursor pela janela para observar como as coordenadas X e Y se comportam!", True, BRANCO)
        tela.blit(info_mouse, (60, 495))
        tela.blit(info_dica, (60, 530))

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
