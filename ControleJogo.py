class jogo:
    def __init__(self,jogador1,jogador2) -> None:
        self.__x = jogador1
        self.__o = jogador2

    def montaJogo(self, dado = None):
        return [[dado,dado,dado],[dado,dado,dado],[dado,dado,dado]]
    
    def jogada(self,jogador, jogo, posL, posC):
        if jogador == self.__x:
            jogoatualizado = jogo[posL[posC]] = "x"
        if jogador == self.__o:
            jogoatualizado = jogo[posL[posC]] = "o"
        return jogoatualizado
    
    def verificaVazio(self, jogo, posL, posC):
        if jogo[posL[posC]] == None:
            return True
        else:
           return False
    
    def verificaSeAcabou(self, jogo):
        for linha in jogo:
            if linha[0] == linha[1] == linha[2]:
                return True
        
        diagonal = []
        for i,linha in len(jogo),jogo:
            for j,coluna in len(linha),linha:
                if i==j:
                    diagonal.append(linha[coluna])
        if diagonal[0] == diagonal[1] == diagonal[2]:
            return True
        
        diagonalInversa = []
        for i,linha in len(jogo),jogo:
            for j,coluna in len(linha),linha:
                if i+j == 4:
                    diagonalInversa.append(linha[coluna])
        if diagonalInversa[0] == diagonalInversa[1] == diagonalInversa[2]:
            return True
        
        reta1 = []
        reta2 = []
        reta3 = []
        for i,linha in len(jogo),jogo:
            for j,coluna in len(linha),linha:
                if j == 0:
                    reta1.append(linha[coluna])
                if j == 1:
                    reta2.append(linha[coluna])
                if j == 2:
                    reta3.append(linha[coluna])
                
        if reta1[0] == reta1[1] == reta1[2]:
            return True
        if reta2[0] == reta2[1] == reta2[2]:
            return True
        if reta3[0] == reta3[1] == reta3[2]:
            return True
        
        return False
