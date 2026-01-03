import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# CONFIGURAÇÕES DA TELA
LARGURA_TELA = 400
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Flappy Bird Clone")

# CORES (RGB - Red, Green, Blue)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL_CEU = (135, 206, 235)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

# CONFIGURAÇÕES DO JOGO
FPS = 60
GRAVIDADE = 0.5
FORCA_PULO = -10
VELOCIDADE_CANOS = 3
DISTANCIA_CANOS = 200
ABERTURA_CANOS = 180

# CLASSE DO PÁSSARO
class Passaro:
    def __init__(self):
        self.x = 80
        self.y = ALTURA_TELA // 2
        self.velocidade = 0
        self.largura = 40
        self.altura = 30
        self.angulo = 0
        
    def pular(self):
        """Faz o pássaro pular"""
        self.velocidade = FORCA_PULO
        
    def atualizar(self):
        """Atualiza a posição e velocidade do pássaro"""
        # Aplica gravidade
        self.velocidade += GRAVIDADE
        self.y += self.velocidade
        
        # Limita a velocidade de queda
        if self.velocidade > 10:
            self.velocidade = 10
            
        # Calcula ângulo de rotação baseado na velocidade
        if self.velocidade < 0:
            self.angulo = 25
        else:
            self.angulo = -25
            
        # Limita o ângulo
        if self.angulo < -90:
            self.angulo = -90
            
    def desenhar(self, tela):
        """Desenha o pássaro na tela"""
        # Cria um retângulo para o corpo
        pygame.draw.rect(tela, AMARELO, (self.x, self.y, self.largura, self.altura))
        # Desenha o olho
        pygame.draw.circle(tela, PRETO, (int(self.x + 30), int(self.y + 10)), 5)
        # Desenha o bico
        pontos_bico = [
            (self.x + self.largura, self.y + 15),
            (self.x + self.largura + 10, self.y + 15),
            (self.x + self.largura + 5, self.y + 20)
        ]
        pygame.draw.polygon(tela, VERMELHO, pontos_bico)
        
    def get_rect(self):
        """Retorna o retângulo de colisão do pássaro"""
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

# CLASSE DOS CANOS
class Cano:
    def __init__(self, x):
        self.x = x
        self.largura = 70
        # Altura aleatória para o cano de cima
        self.altura_cima = random.randint(100, ALTURA_TELA - ABERTURA_CANOS - 100)
        self.altura_baixo = ALTURA_TELA - self.altura_cima - ABERTURA_CANOS
        self.passou = False
        
    def atualizar(self):
        """Move o cano para a esquerda"""
        self.x -= VELOCIDADE_CANOS
        
    def desenhar(self, tela):
        """Desenha os canos na tela"""
        # Cano de cima
        pygame.draw.rect(tela, VERDE, (self.x, 0, self.largura, self.altura_cima))
        # Borda do cano de cima
        pygame.draw.rect(tela, (0, 200, 0), (self.x - 5, self.altura_cima - 20, self.largura + 10, 20))
        
        # Cano de baixo
        y_baixo = self.altura_cima + ABERTURA_CANOS
        pygame.draw.rect(tela, VERDE, (self.x, y_baixo, self.largura, self.altura_baixo))
        # Borda do cano de baixo
        pygame.draw.rect(tela, (0, 200, 0), (self.x - 5, y_baixo, self.largura + 10, 20))
        
    def colidiu(self, passaro):
        """Verifica se o pássaro colidiu com o cano"""
        passaro_rect = passaro.get_rect()
        
        # Retângulo do cano de cima
        cano_cima = pygame.Rect(self.x, 0, self.largura, self.altura_cima)
        # Retângulo do cano de baixo
        cano_baixo = pygame.Rect(self.x, self.altura_cima + ABERTURA_CANOS, 
                                 self.largura, self.altura_baixo)
        
        return passaro_rect.colliderect(cano_cima) or passaro_rect.colliderect(cano_baixo)
    
    def fora_tela(self):
        """Verifica se o cano saiu da tela"""
        return self.x + self.largura < 0

# CLASSE DO CHÃO
class Chao:
    def __init__(self):
        self.y = ALTURA_TELA - 50
        self.x1 = 0
        self.x2 = LARGURA_TELA
        
    def atualizar(self):
        """Move o chão para criar efeito de movimento"""
        self.x1 -= VELOCIDADE_CANOS
        self.x2 -= VELOCIDADE_CANOS
        
        # Quando um chão sai da tela, reposiciona do outro lado
        if self.x1 + LARGURA_TELA < 0:
            self.x1 = self.x2 + LARGURA_TELA
        if self.x2 + LARGURA_TELA < 0:
            self.x2 = self.x1 + LARGURA_TELA
            
    def desenhar(self, tela):
        """Desenha o chão"""
        pygame.draw.rect(tela, (139, 69, 19), (self.x1, self.y, LARGURA_TELA, 50))
        pygame.draw.rect(tela, (139, 69, 19), (self.x2, self.y, LARGURA_TELA, 50))
        # Linha de grama
        pygame.draw.rect(tela, VERDE, (self.x1, self.y, LARGURA_TELA, 10))
        pygame.draw.rect(tela, VERDE, (self.x2, self.y, LARGURA_TELA, 10))

# FUNÇÃO PARA DESENHAR TEXTO
def desenhar_texto(texto, tamanho, cor, x, y, centralizado=True):
    """Desenha texto na tela"""
    fonte = pygame.font.Font(None, tamanho)
    superficie_texto = fonte.render(texto, True, cor)
    retangulo_texto = superficie_texto.get_rect()
    
    if centralizado:
        retangulo_texto.center = (x, y)
    else:
        retangulo_texto.topleft = (x, y)
        
    tela.blit(superficie_texto, retangulo_texto)
    return retangulo_texto

# TELA DE INÍCIO
def tela_inicio():
    """Mostra a tela inicial do jogo"""
    while True:
        tela.fill(AZUL_CEU)
        
        desenhar_texto("FLAPPY BIRD CLONE", 50, PRETO, LARGURA_TELA // 2, 150)
        desenhar_texto("Pressione ESPAÇO para começar", 30, BRANCO, LARGURA_TELA // 2, 300)
        desenhar_texto("ESPAÇO = Pular", 25, PRETO, LARGURA_TELA // 2, 400)
        desenhar_texto("ESC = Sair", 25, PRETO, LARGURA_TELA // 2, 440)
        
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# TELA DE GAME OVER
def tela_game_over(pontos, recorde):
    """Mostra a tela de game over"""
    while True:
        tela.fill(AZUL_CEU)
        
        desenhar_texto("GAME OVER!", 60, VERMELHO, LARGURA_TELA // 2, 150)
        desenhar_texto(f"Pontuação: {pontos}", 40, PRETO, LARGURA_TELA // 2, 250)
        desenhar_texto(f"Recorde: {recorde}", 40, PRETO, LARGURA_TELA // 2, 300)
        desenhar_texto("Pressione ESPAÇO para jogar novamente", 25, BRANCO, LARGURA_TELA // 2, 400)
        desenhar_texto("ESC = Sair", 25, PRETO, LARGURA_TELA // 2, 450)
        
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return True
                if evento.key == pygame.K_ESCAPE:
                    return False

# FUNÇÃO PRINCIPAL DO JOGO
def jogo():
    """Função principal que roda o jogo"""
    clock = pygame.time.Clock()
    recorde = 0
    
    while True:
        # Mostra tela inicial
        tela_inicio()
        
        # Inicializa objetos do jogo
        passaro = Passaro()
        canos = [Cano(LARGURA_TELA + 200)]
        chao = Chao()
        pontos = 0
        game_over = False
        
        # Loop principal do jogo
        while not game_over:
            clock.tick(FPS)
            
            # Verifica eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        passaro.pular()
                    if evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            # Atualiza pássaro
            passaro.atualizar()
            
            # Verifica colisão com chão e teto
            if passaro.y + passaro.altura >= chao.y or passaro.y <= 0:
                game_over = True
            
            # Atualiza e gerencia canos
            for cano in canos:
                cano.atualizar()
                
                # Verifica colisão com cano
                if cano.colidiu(passaro):
                    game_over = True
                
                # Adiciona ponto quando passa pelo cano
                if not cano.passou and cano.x + cano.largura < passaro.x:
                    cano.passou = True
                    pontos += 1
                    
                    # Atualiza recorde
                    if pontos > recorde:
                        recorde = pontos
            
            # Remove canos que saíram da tela
            canos = [cano for cano in canos if not cano.fora_tela()]
            
            # Adiciona novo cano quando necessário
            if len(canos) == 0 or canos[-1].x < LARGURA_TELA - DISTANCIA_CANOS:
                canos.append(Cano(LARGURA_TELA))
            
            # Atualiza chão
            chao.atualizar()
            
            # DESENHA TUDO
            tela.fill(AZUL_CEU)
            
            # Desenha canos
            for cano in canos:
                cano.desenhar(tela)
            
            # Desenha chão
            chao.desenhar(tela)
            
            # Desenha pássaro
            passaro.desenhar(tela)
            
            # Desenha pontuação
            desenhar_texto(f"Pontos: {pontos}", 40, BRANCO, 70, 30, centralizado=False)
            desenhar_texto(f"Recorde: {recorde}", 30, BRANCO, 70, 70, centralizado=False)
            
            pygame.display.flip()
        
        # Mostra tela de game over
        jogar_novamente = tela_game_over(pontos, recorde)
        if not jogar_novamente:
            break
    
    pygame.quit()
    sys.exit()

# INICIA O JOGO
if __name__ == "__main__":
    jogo()