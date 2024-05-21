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
        jogoPai = self.__jogo.montaJogo(jogosfilho)
        self.__telaDoJogo.mostraJogo(jogoPai)

        while True:
            #=========================  VEZ JOGADOR 1 ==========================================================
            posPaiL, posPaiC, posFilhoL, posFilhoC = self.__telaDoJogo.perguntaJogada(self.__jogador1)
            jogadaValida = self.__jogo.verificaVazio(jogoPai[posPaiL[posPaiC]],posFilhoL,posFilhoC)
            if jogadaValida == True:
                jogoPai[posPaiL[posPaiC]] = self.__jogo.jogada(self.__jogador1,jogoPai[posPaiL[posPaiC]],posFilhoL,posFilhoC)
                self.__telaDoJogo.mostraJogo(jogoPai)

                #============== VERIFICA SE JOGO MENOR ACABOU ===================================================
                if self.__jogo.verificaSeAcabou(jogoPai[posPaiL[posPaiC]])  == True:
                    jogoPai = self.__jogo.jogada(self.__jogador1,jogoPai,posPaiL,posPaiC)
                    self.__telaDoJogo.aviso("Jogofilho finalizado")
                    self.__telaDoJogo.mostraJogo(jogoPai)

                #================= vERIFICA SE O JOGO PAI ACABOU =================================================
                if self.__jogo.verificaSeAcabou(jogoPai) == True:
                    break
            else:
                self.__telaDoJogo.aviso("Jogada Invalida")



            #=========================  VEZ JOGADOR 2 ============================================================
            posPaiL, posPaiC, posFilhoL, posFilhoC = self.__telaDoJogo.perguntaJogada(self.__jogador2)
            jogadaValida = self.__jogo.verificaVazio(jogoPai[posPaiL[posPaiC]],posFilhoL,posFilhoC)
            if jogadaValida == True:
                jogoPai[posPaiL[posPaiC]] = self.__jogo.jogada(self.__jogador2,jogoPai[posPaiL[posPaiC]],posFilhoL,posFilhoC)
                self.__telaDoJogo.mostraJogo(jogoPai)

                #============== VERIFICA SE JOGO MENOR ACABOU ===================================================
                if self.__jogo.verificaSeAcabou(jogoPai[posPaiL[posPaiC]])  == True:
                    jogoPai = self.__jogo.jogada(self.__jogador2,jogoPai,posPaiL,posPaiC)
                    self.__telaDoJogo.aviso("Jogofilho finalizado")
                    self.__telaDoJogo.mostraJogo(jogoPai)

                #================= vERIFICA SE O JOGO PAI ACABOU =================================================
                if self.__jogo.verificaSeAcabou(jogoPai) == True:
                    break
            else:
                self.__telaDoJogo.aviso("Jogada Invalida")


