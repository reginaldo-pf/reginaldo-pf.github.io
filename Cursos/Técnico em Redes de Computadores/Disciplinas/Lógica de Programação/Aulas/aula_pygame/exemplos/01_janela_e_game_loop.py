"""
Aula 01: Introducao ao Pygame
Exemplo 01: Janela Basica e Game Loop (Laco Principal)

Conceitos abordados:
1. Inicializacao do Pygame (pygame.init)
2. Criacao da janela/superficie principal (pygame.display.set_mode)
3. O Game Loop: Eventos -> Atualizacao -> Desenho -> Relogio
4. O evento de fechamento da janela (pygame.QUIT)
5. Encerramento seguro (pygame.quit, sys.exit)
"""

import pygame
import sys

def main():
    # 1. INICIALIZACAO
    # Inicializa todos os modulos internos do Pygame (video, audio, fontes, etc.)
    pygame.init()

    # Dimensoes da janela em pixels (Largura, Altura)
    LARGURA = 800
    ALTURA = 600
    
    # Cria a janela do jogo (Surface principal onde tudo sera desenhado)
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    
    # Define o titulo que aparece na barra superior da janela
    pygame.display.set_caption("Pygame - Exemplo 01: Estrutura Basica e Game Loop")

    # Objeto Relogio para controlar a taxa de atualizacao (FPS)
    relogio = pygame.time.Clock()

    # Definicao de cores no formato RGB (Red, Green, Blue) variando de 0 a 255
    COR_FUNDO = (30, 35, 45)  # Azul escuro grafite

    # Variavel de controle do laco principal
    executando = True

    # 2. O GAME LOOP (LACO PRINCIPAL)
    # Roda continuamente enquanto o jogo estiver ativo (~60 vezes por segundo)
    while executando:
        
        # --- ETAPA A: PROCESSAMENTO DE ENTRADAS / EVENTOS ---
        # Percorre a fila de eventos do sistema operacional (cliques, teclas, fechar janela)
        for evento in pygame.event.get():
            # Se o usuario clicar no 'X' para fechar a janela:
            if evento.type == pygame.QUIT:
                executando = False

        # --- ETAPA B: ATUALIZACAO DA LOGICA DO JOGO ---
        # (Neste exemplo introdutorio ainda nao temos objetos se movendo)

        # --- ETAPA C: RENDERIZACAO / DESENHO ---
        # Limpa a tela pintando-a com a cor de fundo
        tela.fill(COR_FUNDO)

        # Atualiza o monitor com o que acabamos de desenhar (Double Buffering)
        pygame.display.flip()

        # --- ETAPA D: CONTROLE DE TEMPO (FPS) ---
        # Garante que o laco execute a no maximo 60 quadros por segundo
        relogio.tick(60)

    # 3. FINALIZACAO
    # Desliga os modulos do Pygame e encerra o processo do Python
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
