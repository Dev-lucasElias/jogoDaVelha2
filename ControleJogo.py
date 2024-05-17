class jogo:
    def __init__(self,jogador1,jogador2) -> None:
        self.__x = jogador1
        self.__o = jogador2

    def montaJogo(self, dado = None):
        return [[dado,dado,dado],[dado,dado,dado],[dado,dado,dado]]
    
    def jogada(self,jogador, jogo, posicao):
        if jogador == self.__x:
            jogoatualizado = jogo[posicao] = "x"
        else:
            jogoatualizado = jogo[posicao] = "o"
        return jogoatualizado