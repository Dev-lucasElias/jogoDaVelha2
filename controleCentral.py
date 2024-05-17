from interface import Tela


class ControleCentral:

    def __init__(self) -> None:
        self.__jogador1 = None
        self.__jogador2 = None
        self.__telaDoJogo = Tela()


    def iniciaJogo(self):
        self.__jogador1 = self.__telaDoJogo.perguntaNomejogador1()
        self.__jogador2 = self.__telaDoJogo.perguntaNomejogador2()
        