"""
Aula 01: Introducao ao Pygame
Exemplo 05 (Projeto Integrador): Mini-Jogo "Caca aos Cristais"

Conceitos consolidados:
1. Game Loop completo com maquina de estados simples (JOGANDO e GAME_OVER)
2. Criacao e manipulacao de retangulos com 'pygame.Rect'
3. Deteccao de colisao entre retangulos usando 'rect1.colliderect(rect2)'
4. Geracao de numeros aleatorios com a biblioteca padrao 'random'
5. Renderizacao de texto com fontes (HUD de pontos e tempo restante)
6. Sintese de audio procedural direto na memoria (sem arquivos externos!)
7. Logica de reinicio de partida (pressionar 'R')
"""

import pygame
import sys
import random
import math
import array

# --- FUNCAO AUXILIAR PARA GERAR SONS SEM PRECISAR DE ARQUIVOS EXTERNOS ---
def criar_som_bip(frequencia=880, duracao=0.08, volume=0.3):
    """Gera um som sintetizado matematicamente via onda senoidal na memoria."""
    taxa_amostragem = 44100
    total_amostras = int(taxa_amostragem * duracao)
    amostras = array.array('h')
    
    for i in range(total_amostras):
        # Onda senoidal com decaimento suave para nao dar estalo
        envelope = 1.0 - (i / total_amostras)
        valor = int(32767 * volume * envelope * math.sin(2.0 * math.pi * frequencia * (i / taxa_amostragem)))
        amostras.append(valor)
        
    return pygame.mixer.Sound(buffer=amostras)

def main():
    # 1. INICIALIZACAO COMPLETA
    pygame.init()
    pygame.mixer.init(44100, -16, 1, 512)

    LARGURA = 800
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Pygame - Projeto: Caca aos Cristais!")
    relogio = pygame.time.Clock()

    # Sons sintetizados para eventos do jogo
    som_coleta = criar_som_bip(frequencia=988, duracao=0.10, volume=0.4)    # Som agudo alegre
    som_dano   = criar_som_bip(frequencia=220, duracao=0.18, volume=0.5)    # Som grave de alerta

    # Cores (Paleta moderna 2D)
    COR_FUNDO    = (20, 24, 36)
    COR_JOGADOR  = (88, 166, 255)   # Ciano/Azul
    COR_CRISTAL  = (255, 215, 0)    # Amarelo Ouro
    COR_PERIGO   = (255, 80, 80)    # Vermelho Alerta
    COR_TEXTO    = (240, 246, 252)
    COR_PAINEL   = (30, 36, 52)

    # Fontes
    fonte_hud = pygame.font.SysFont("Arial", 22, bold=True)
    fonte_titulo = pygame.font.SysFont("Arial", 46, bold=True)
    fonte_subtitulo = pygame.font.SysFont("Arial", 20)

    # --- FUNCAO PARA REINICIAR AS VARIAVEIS DA PARTIDA ---
    def reiniciar_jogo():
        jogador = pygame.Rect(LARGURA // 2 - 20, ALTURA // 2 - 20, 40, 40)
        
        # Cristal inicial em posicao aleatoria (com margem das bordas)
        cristal = pygame.Rect(
            random.randint(50, LARGURA - 70),
            random.randint(90, ALTURA - 70),
            24, 24
        )

        # Obstaculo perigoso que rebate pelas paredes
        obstaculo = pygame.Rect(100, 100, 32, 32)
        vel_obstaculo = [5.0, 4.0]

        pontuacao = 0
        duracao_total = 30.0  # Partida de 30 segundos
        tempo_inicio = pygame.time.get_ticks() / 1000.0
        estado = "JOGANDO"

        return jogador, cristal, obstaculo, vel_obstaculo, pontuacao, duracao_total, tempo_inicio, estado

    # Inicializa variaveis do jogo
    jogador, cristal, obstaculo, vel_obstaculo, pontuacao, duracao_total, tempo_inicio, estado = reiniciar_jogo()
    vel_jogador = 6

    # 2. GAME LOOP PRINCIPAL
    executando = True
    while executando:
        
        # A. PROCESSAMENTO DE EVENTOS
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            
            elif evento.type == pygame.KEYDOWN:
                # Se estiver na tela final de Game Over, 'R' reinicia a partida
                if estado == "GAME_OVER" and evento.key == pygame.K_r:
                    jogador, cristal, obstaculo, vel_obstaculo, pontuacao, duracao_total, tempo_inicio, estado = reiniciar_jogo()

        # B. LOGICA DO JOGO (Apenas se o jogo estiver em andamento)
        if estado == "JOGANDO":
            # 1. Calculo do tempo restante
            tempo_decorrido = (pygame.time.get_ticks() / 1000.0) - tempo_inicio
            tempo_restante = max(0.0, duracao_total - tempo_decorrido)

            if tempo_restante <= 0:
                estado = "GAME_OVER"

            # 2. Movimentacao contigua do jogador (Setas ou WASD)
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                jogador.x -= vel_jogador
            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                jogador.x += vel_jogador
            if teclas[pygame.K_UP] or teclas[pygame.K_w]:
                jogador.y -= vel_jogador
            if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
                jogador.y += vel_jogador

            # 3. Bloqueio nas bordas da janela (deixando espaco para o painel do topo)
            jogador.left = max(0, jogador.left)
            jogador.right = min(LARGURA, jogador.right)
            jogador.top = max(70, jogador.top)  # Barra de HUD fica acima de 70px
            jogador.bottom = min(ALTURA, jogador.bottom)

            # 4. Movimento e quique do obstaculo perigoso
            obstaculo.x += int(vel_obstaculo[0])
            obstaculo.y += int(vel_obstaculo[1])

            if obstaculo.left <= 0 or obstaculo.right >= LARGURA:
                vel_obstaculo[0] *= -1
            if obstaculo.top <= 70 or obstaculo.bottom >= ALTURA:
                vel_obstaculo[1] *= -1

            # 5. Deteccao de Colisao: Jogador coletou o Cristal?
            if jogador.colliderect(cristal):
                pontuacao += 10
                som_coleta.play()
                # Reposiciona o cristal em novo ponto seguro
                cristal.x = random.randint(50, LARGURA - 70)
                cristal.y = random.randint(90, ALTURA - 70)

            # 6. Deteccao de Colisao: Jogador tocou no Obstaculo?
            if jogador.colliderect(obstaculo):
                pontuacao = max(0, pontuacao - 5)
                som_dano.play()
                # Afasta o obstaculo para evitar dano continuo no mesmo ponto
                obstaculo.x = random.randint(50, LARGURA - 70)
                obstaculo.y = random.randint(90, ALTURA - 70)

        # C. RENDERIZACAO / DESENHO
        tela.fill(COR_FUNDO)

        if estado == "JOGANDO":
            # Desenha o cristal (com efeito de diamante ou circulo dourado)
            pygame.draw.rect(tela, COR_CRISTAL, cristal, border_radius=4)
            pygame.draw.circle(tela, (255, 255, 200), cristal.center, 4)

            # Desenha o obstaculo perigoso (vermelho)
            pygame.draw.rect(tela, COR_PERIGO, obstaculo, border_radius=6)
            pygame.draw.circle(tela, (255, 200, 200), obstaculo.center, 5)

            # Desenha o jogador
            pygame.draw.rect(tela, COR_JOGADOR, jogador, border_radius=8)
            pygame.draw.circle(tela, (255, 255, 255), jogador.center, 7)

            # --- HUD (BARRA SUPERIOR DE INFORMACOES) ---
            pygame.draw.rect(tela, COR_PAINEL, (0, 0, LARGURA, 70))
            pygame.draw.line(tela, (50, 60, 85), (0, 70), (LARGURA, 70), 2)

            txt_pts = fonte_hud.render(f"Pontos: {pontuacao}", True, COR_CRISTAL)
            txt_tempo = fonte_hud.render(f"Tempo: {tempo_restante:.1f}s", True, COR_TEXTO if tempo_restante > 5 else COR_PERIGO)
            txt_guia = fonte_subtitulo.render("Colete os cristais [Amarelo] e evite a armadilha [Vermelho]!", True, (160, 175, 200))

            tela.blit(txt_pts, (30, 20))
            tela.blit(txt_tempo, (220, 20))
            tela.blit(txt_guia, (400, 23))

        elif estado == "GAME_OVER":
            # Tela final escura com destaque para a pontuacao final
            painel_box = pygame.Rect(150, 120, 500, 360)
            pygame.draw.rect(tela, COR_PAINEL, painel_box, border_radius=16)
            pygame.draw.rect(tela, COR_JOGADOR, painel_box, width=3, border_radius=16)

            txt_fim = fonte_titulo.render("TEMPO ESGOTADO!", True, COR_PERIGO)
            txt_final_pts = fonte_hud.render(f"Sua Pontuacao Final: {pontuacao} pontos", True, COR_CRISTAL)
            txt_restart = fonte_subtitulo.render("Pressione [ R ] para Jogar Novamente", True, COR_TEXTO)
            txt_sair = fonte_subtitulo.render("Pressione o [ X ] da janela para encerrar", True, (150, 160, 180))

            # Centraliza os textos na caixa
            tela.blit(txt_fim, txt_fim.get_rect(center=(LARGURA // 2, 200)))
            tela.blit(txt_final_pts, txt_final_pts.get_rect(center=(LARGURA // 2, 270)))
            tela.blit(txt_restart, txt_restart.get_rect(center=(LARGURA // 2, 350)))
            tela.blit(txt_sair, txt_sair.get_rect(center=(LARGURA // 2, 400)))

        pygame.display.flip()
        relogio.tick(60)

    # 3. ENCERRAMENTO
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
