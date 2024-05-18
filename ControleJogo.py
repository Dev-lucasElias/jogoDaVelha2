class jogo:
    def __init__(self,jogador1,jogador2) -> None:
        self.__x = jogador1
        self.__o = jogador2

    def montaJogo(self, dado = None):
        return [[dado,dado,dado],[dado,dado,dado],[dado,dado,dado]]
    
    def jogada(self,jogador, jogo, posL, posC):
        if jogador == self.__x:
            jogoatualizado = jogo[posL[posC]] = "x"
        else:
            jogoatualizado = jogo[posL[posC]] = "o"
        return jogoatualizado
    
    def verificaVazio(self, jogo, posL, posC):
        if jogo[posL[posC]] == None:
            return True
        else:
           return False
    
    def verificaSeAcabou(self, jogo):
        pass