from interface import Tela
from ControleJogo import jogo

class ControleCentral:

    def __init__(self) -> None:
        self.__jogador1 = None
        self.__jogador2 = None
        self.__telaDoJogo = Tela()
        self.__jogo = jogo()


    def iniciaJogo(self):
        self.__jogador1 = self.__telaDoJogo.perguntaNomejogador1()
        self.__jogador2 = self.__telaDoJogo.perguntaNomejogador2()
        jogosfilho = self.__jogo.montaJogo(None)
        jogoPai = []
        for i in jogosfilho:
            jogoPai.append(self.__jogo.montaJogo(i))
        
        