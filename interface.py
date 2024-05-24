from pygame.locals import pygame as py
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN
)


class Tela:
    def __init__(self) -> None:
        py.init()
        self.widthScreen = 800
        self.heightScreen = 800
        self.__screen = py.display.set_mode((self.widthScreen, self.heightScreen))
        self.__screen.fill("white")
        py.display.flip()
        self.running = True
        self.__branco = (255, 255, 255)
        self.__preto = (0, 0, 0)
        self.__vermelho = (255, 0, 0)
        

    def perguntaNomejogador1(self):
        while self.running:
            for event in py.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                elif event.type == QUIT:
                    self.running = False


    def perguntaNomejogador2(self):
        while self.running:
            for event in py.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                elif event.type == QUIT:
                    running = False

    def perguntaJogada(self, jogador):
        while self.running:
            for event in py.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                elif event.type == QUIT:
                    self.running = False

    def mostraJogo(self, jogo = None):
        widhtPai = 600
        heightPai = 600
        offset_x = (self.widthScreen - widhtPai) // 2
        offset_y = (self.heightScreen - heightPai) // 2
        py.draw.line(self.__screen, self.__preto, (offset_x, offset_y + int(widhtPai/3)), (offset_x + heightPai, offset_y + widhtPai/3), 5)
        py.draw.line(self.__screen, self.__preto, (offset_x, offset_y + (widhtPai/3)*2), (offset_x + heightPai, offset_y + (widhtPai/3)*2), 5)
        py.draw.line(self.__screen, self.__preto, (offset_x + (heightPai/3) , offset_y), (offset_x+(heightPai/3), offset_y+widhtPai), 5)
        py.draw.line(self.__screen, self.__preto, (offset_x+(heightPai/3)*2, offset_y), (offset_x+(heightPai/3)*2, offset_y + widhtPai), 5)
        self.__screen.blit(self.montaTabuleirofilho(int(widhtPai/3),int(heightPai/3)), (0, 0))
        self.__screen.blit(self.montaTabuleirofilho(int(widhtPai/3),int(heightPai/3)), (0, int(widhtPai/3)))
        self.__screen.blit(self.montaTabuleirofilho(int(widhtPai/3),int(heightPai/3)), (0, int((widhtPai/3)*2)))
        self.__screen.blit(self.montaTabuleirofilho(int(widhtPai/3),int(heightPai/3)), (int(heightPai/3), 0))
        self.__screen.blit(self.montaTabuleirofilho(int(widhtPai/3),int(heightPai/3)), (int(heightPai/3), int(widhtPai/3)))
        self.__screen.blit(self.montaTabuleirofilho(int(widhtPai/3),int(heightPai/3)), (int(heightPai/3), int((widhtPai/3)*2)))
        self.__screen.blit(self.montaTabuleirofilho(int(widhtPai/3),int(heightPai/3)), (int((heightPai/3)*2), 0))
        self.__screen.blit(self.montaTabuleirofilho(int(widhtPai/3),int(heightPai/3)), (int((heightPai/3)*2), int(widhtPai/3)))
        self.__screen.blit(self.montaTabuleirofilho(int(widhtPai/3),int(heightPai/3)), (int((heightPai/3)*2), int((widhtPai/3)*2)))
        py.display.flip()
        while self.running:
            for event in py.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                elif event.type == QUIT:
                    self.running = False

    def aviso(self, msg):
        pass

    def montaTabuleirofilho(self,width, height):
        tabuleiro_filho = py.Surface((width,height))
        tabuleiro_filho.fill(self.__branco)
        py.draw.line(tabuleiro_filho, self.__preto, (0,int(width/3)), (height,int(width/3)), 2)
        py.draw.line(tabuleiro_filho, self.__preto, (0,(int(width/3)*2)), (height,int((width/3)*2)), 2)
        py.draw.line(tabuleiro_filho, self.__preto, (int(height/3),0), (int(height/3), width), 2)
        py.draw.line(tabuleiro_filho, self.__preto, (int((height/3)*2),0), (int((height/3)*2),width), 2)
        botao11 = Botaojogada("Jogar", (100, 150, 50), (50, 100, 150), self.__branco, 0, 0, height/3, width/100).desenhar(tabuleiro_filho)
        botao12 = Botaojogada("Jogar", (100, 150, 50), (50, 100, 150), self.__branco, 0, width/3, height/3, width/3).desenhar(tabuleiro_filho)
        botao13 = Botaojogada("Jogar", (100, 150, 50), (50, 100, 150), self.__branco, 0, (width/3)*2, height/3, width/3).desenhar(tabuleiro_filho)
        botao21 = Botaojogada("Jogar", (100, 150, 50), (50, 100, 150), self.__branco, height/3, 0, height/3, width/3).desenhar(tabuleiro_filho)
        botao22 = Botaojogada("Jogar", (100, 150, 50), (50, 100, 150), self.__branco, height/3, width/3, height/3, width/3).desenhar(tabuleiro_filho)
        botao23 = Botaojogada("Jogar", (100, 150, 50), (50, 100, 150), self.__branco, height/3, (width/3)*2, height/3, width/3).desenhar(tabuleiro_filho)
        botao31 = Botaojogada("Jogar", (100, 150, 50), (50, 100, 150), self.__branco, (height/3)*2, 0, height/3, width/3).desenhar(tabuleiro_filho)
        botao32 = Botaojogada("Jogar", (100, 150, 50), (50, 100, 150), self.__branco, (height/3)*2, width/3, height/3, width/3).desenhar(tabuleiro_filho)
        botao33 = Botaojogada("Jogar", (100, 150, 50), (50, 100, 150), self.__branco, (height/3)*2, (width/3)*2, height/3, width/3).desenhar(tabuleiro_filho)
        py.display.flip()
        return tabuleiro_filho 

        
class Botaojogada:
    def __init__(self, texto, cor_inativa, cor_ativa, cor_texto, x, y, largura, altura):
        self.texto = texto
        self.cor_inativa = cor_inativa
        self.cor_ativa = cor_ativa
        self.cor_texto = cor_texto
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.fonte = py.font.SysFont(None, 30)
        self.rect = py.Rect(self.x, self.y, self.largura, self.altura)
        self.ativo = False

    def desenhar(self, tela):
        cor = self.cor_ativa if self.ativo else self.cor_inativa
        py.draw.rect(tela, cor, self.rect)
        texto_renderizado = self.fonte.render(self.texto, True, self.cor_texto)
        rect_texto = texto_renderizado.get_rect(center=self.rect.center)
        tela.blit(texto_renderizado, rect_texto)

    def atualizar(self, evento):
        if evento.type == MOUSEBUTTONDOWN and evento.pos in self.rect.topleft:
            self.ativo = not self.ativo

    def checar_clique_botao(botoes, evento):
        for botao in botoes:
            botao.atualizar(evento)
            if botao.ativo:
                return botao
        return None

tela1 = Tela()
tela1.mostraJogo()
