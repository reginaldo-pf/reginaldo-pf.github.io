"""
Aula 01: Introducao ao Pygame
Exemplo 04: Interatividade, Teclado e Bloqueio de Bordas

Conceitos abordados:
1. Captura de teclas continuas com 'pygame.key.get_pressed()'
   - Diferenca entre evento pontual (KEYDOWN) vs tecla mantida pressionada
2. Suporte simultaneo a Setas direcionais e WASD
3. Limitacao de borda (Border Clamping): impedir que o objeto saia da tela
4. Utilizacao da classe pygame.Rect para representar entidades do jogo
"""

import pygame
import sys

def main():
    pygame.init()

    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Pygame - Exemplo 04: Controle por Teclado e Bordas")
    relogio = pygame.time.Clock()

    COR_FUNDO  = (22, 27, 34)
    AZUL_HEROI = (88, 166, 255)
    VERDE_BORDA = (63, 185, 80)
    BRANCO     = (240, 246, 252)
    CINZA      = (139, 148, 158)
    AMARELO    = (210, 153, 34)

    # Criando nosso personagem como um objeto pygame.Rect
    # Parametros: (posicao_x_inicial, posicao_y_inicial, largura, altura)
    jogador_tam = 50
    jogador = pygame.Rect(375, 275, jogador_tam, jogador_tam)
    velocidade = 6  # Pixels percorridos a cada frame

    fonte = pygame.font.SysFont("Arial", 18, bold=True)
    fonte_pequena = pygame.font.SysFont("Arial", 14)

    contador_saltos = 0  # Exemplo de evento pontual (barra de espaco)

    executando = True
    while executando:
        # 1. PROCESSAMENTO DE EVENTOS PONTUAIS (Fila de Eventos)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            
            elif evento.type == pygame.KEYDOWN:
                # Eventos unicos: perfeitos para acoes instantaneas (ex: pular, atirar, pausar)
                if evento.key == pygame.K_SPACE:
                    contador_saltos += 1

        # 2. CAPTURA DE TECLAS CONTINUAS (Para movimentacao fluida)
        # Retorna uma sequencia booleana com o estado de todas as teclas do teclado
        teclas = pygame.key.get_pressed()

        # Movimento Horizontal (Esquerda / Direita)
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            jogador.x -= velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jogador.x += velocidade

        # Movimento Vertical (Cima / Baixo)
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            jogador.y -= velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            jogador.y += velocidade

        # 3. LIMITACAO DE BORDAS (BORDER CLAMPING)
        # Impede que o retangulo atravesse as extremidades da janela
        if jogador.left < 0:
            jogador.left = 0
        if jogador.right > LARGURA:
            jogador.right = LARGURA
        if jogador.top < 0:
            jogador.top = 0
        if jogador.bottom > ALTURA:
            jogador.bottom = ALTURA

        # 4. RENDERIZACAO
        tela.fill(COR_FUNDO)

        # Desenha uma moldura nas bordas da tela
        pygame.draw.rect(tela, VERDE_BORDA, (0, 0, LARGURA, ALTURA), width=3)

        # Desenha o jogador (quadrado com cantos arredondados)
        pygame.draw.rect(tela, AZUL_HEROI, jogador, border_radius=6)
        # Desenha um detalhe no centro do jogador
        pygame.draw.circle(tela, BRANCO, jogador.center, 8)

        # Painel Superior de Instrucoes e Telemetria
        painel = pygame.Rect(20, 20, 760, 80)
        pygame.draw.rect(tela, (13, 17, 23), painel, border_radius=8)
        pygame.draw.rect(tela, CINZA, painel, width=1, border_radius=8)

        txt_info = fonte.render(f"Posicao do Jogador: X = {jogador.x} | Y = {jogador.y} | Cliques no Espaco: {contador_saltos}", True, AMARELO)
        txt_ajuda = fonte_pequena.render("Use as SETAS ou WASD para movimentar o personagem suavemente pela tela.", True, BRANCO)
        txt_dica2 = fonte_pequena.render("Observe como o personagem e bloqueado ao alcancar as bordas da janela.", True, CINZA)

        tela.blit(txt_info, (40, 30))
        tela.blit(txt_ajuda, (40, 52))
        tela.blit(txt_dica2, (40, 70))

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
