from pygame.locals import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Tela:
    def __init__(self) -> None:
        pygame.init()
        self.__screen = pygame.display.set_mode((1280, 720))
        self.__screen.fill("white")
        pygame.display.flip()
        self.running = True
        self.player1_image = pygame.image.load('imgjogo.png')
        

    def perguntaNomejogador1(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                elif event.type == QUIT:
                    self.running = False


    def perguntaNomejogador2(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                elif event.type == QUIT:
                    running = False

    def perguntaJogada(self, jogador):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                elif event.type == QUIT:
                    self.running = False

    def mostraJogo(self, jogo = None):
        pygame.draw.aaline(self.__screen, (60, 179, 113), [0, 50], [50, 80], True)
        pygame.Surface((75, 25))
        pygame.blit(self.player1_image,(0, 0))
        pygame.display.flip()
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                elif event.type == QUIT:
                    self.running = False

    def aviso(self, msg):
        pass


tela1 = Tela()
tela1.mostraJogo()
