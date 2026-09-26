"""
Aula 01: Introducao ao Pygame
Exemplo 03: Animacao, Taxa de Quadros (FPS) e Limpeza de Tela

Conceitos abordados:
1. Como funciona a ilusao de movimento:
   - Posicao atualizada a cada ciclo: pos = pos + velocidade
2. Inversao de movimento (rebote contra as bordas da tela)
3. Por que precisamos do 'tela.fill()'?
   - Pressione [ESPACO] para alternar entre limpar a tela ou deixar o rastro!
4. O papel do clock.tick(FPS):
   - Pressione [F] para alternar entre 60 FPS, 30 FPS, 15 FPS e 120 FPS.
"""

import pygame
import sys

def main():
    pygame.init()

    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Pygame - Exemplo 03: Animacao, FPS e Limpeza de Tela")
    relogio = pygame.time.Clock()

    # Cores
    COR_FUNDO = (25, 30, 42)
    BRANCO    = (255, 255, 255)
    VERMELHO  = (240, 80, 80)
    AMARELO   = (255, 215, 0)
    VERDE     = (80, 220, 120)
    CIANO     = (60, 200, 240)

    # Propriedades do objeto em movimento (Bolinha)
    raio = 24
    pos_x = 100.0
    pos_y = 150.0
    vel_x = 5.0
    vel_y = 4.0

    # Variaveis interativas para demonstracao em sala
    limpar_tela = True
    fps_opcoes = [60, 30, 15, 120]
    indice_fps = 0

    fonte = pygame.font.SysFont("Arial", 18, bold=True)
    fonte_pequena = pygame.font.SysFont("Arial", 14)

    executando = True
    while executando:
        # 1. PROCESSAMENTO DE EVENTOS
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            
            # Captura de teclas pontuais (KEYDOWN)
            elif evento.type == pygame.KEYDOWN:
                # Barra de espaco ativa/desativa a limpeza de tela
                if evento.key == pygame.K_SPACE:
                    limpar_tela = not limpar_tela
                # Tecla F altera o limite de FPS
                elif evento.key == pygame.K_f:
                    indice_fps = (indice_fps + 1) % len(fps_opcoes)

        # 2. ATUALIZACAO DA FISICA / MOVIMENTO
        pos_x += vel_x
        pos_y += vel_y

        # Verificacao de colisoes com as bordas horizontais (Esquerda e Direita)
        if pos_x + raio >= LARGURA:
            pos_x = LARGURA - raio
            vel_x = -vel_x  # Inverte o sentido horizontal
        elif pos_x - raio <= 0:
            pos_x = raio
            vel_x = -vel_x

        # Verificacao de colisoes com as bordas verticais (Topo e Base)
        if pos_y + raio >= ALTURA:
            pos_y = ALTURA - raio
            vel_y = -vel_y  # Inverte o sentido vertical
        elif pos_y - raio <= 0:
            pos_y = raio
            vel_y = -vel_y

        # 3. RENDERIZACAO
        # Se a limpeza estiver ativa, pintamos o fundo. Se nao, o rastro permanece!
        if limpar_tela:
            tela.fill(COR_FUNDO)

        # Desenha a bolinha na posicao atual
        pygame.draw.circle(tela, VERMELHO, (int(pos_x), int(pos_y)), raio)
        pygame.draw.circle(tela, BRANCO, (int(pos_x), int(pos_y)), raio, width=2)

        # Painel fixo de informacoes
        painel_hud = pygame.Rect(10, 10, 390, 120)
        pygame.draw.rect(tela, (15, 18, 26), painel_hud, border_radius=8)
        pygame.draw.rect(tela, CIANO, painel_hud, width=2, border_radius=8)

        status_limpeza = "ATIVADA (Normal)" if limpar_tela else "DESATIVADA (Efeito Rastro!)"
        cor_limpeza = VERDE if limpar_tela else AMARELO
        fps_atual = fps_opcoes[indice_fps]

        txt1 = fonte.render(f"FPS Alvo: {fps_atual} quadros/segundo", True, BRANCO)
        txt2 = fonte.render(f"Limpeza de Tela: {status_limpeza}", True, cor_limpeza)
        txt3 = fonte_pequena.render("[ESPACO] Alternar tela.fill() (Ver rastro)", True, CIANO)
        txt4 = fonte_pequena.render("[F] Alternar limite de FPS", True, CIANO)

        tela.blit(txt1, (25, 20))
        tela.blit(txt2, (25, 45))
        tela.blit(txt3, (25, 75))
        tela.blit(txt4, (25, 98))

        pygame.display.flip()

        # 4. SINCRONIZACAO COM O RELOGIO
        relogio.tick(fps_atual)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
