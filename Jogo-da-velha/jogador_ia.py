from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)
        self.oponente = Tabuleiro.JOGADOR_X if tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

    def getJogada(self) -> (int, int):
        # regra 1
        jogada = self.verificar_vitoria_ou_bloqueio(self.tipo) or self.verificar_vitoria_ou_bloqueio(self.oponente)
        if jogada:
            return jogada

        # regra 2
        jogada = self.criar_dupla_sequencia()
        if jogada:
            return jogada

        # regra 3
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # regra 4
        jogada = self.marcar_canto_oposto()
        if jogada:
            return jogada

        # regra 5
        jogada = self.marcar_canto_vazio()
        if jogada:
            return jogada

        # regra 6
        return self.marcar_aleatoriamente()

    def verificar_vitoria_ou_bloqueio(self, tipo: int) -> (int, int):
        for i in range(3):
            # linhas
            if self.matriz[i].count(tipo) == 2 and Tabuleiro.DESCONHECIDO in self.matriz[i]:
                return (i, self.matriz[i].index(Tabuleiro.DESCONHECIDO))
            
            # as colunas
            coluna = [self.matriz[j][i] for j in range(3)]
            if coluna.count(tipo) == 2 and Tabuleiro.DESCONHECIDO in coluna:
                return (coluna.index(Tabuleiro.DESCONHECIDO), i)
            
        # verficando diagonais 
        diagonal1 = [self.matriz[i][i] for i in range(3)]
        diagonal2 = [self.matriz[i][2 - i] for i in range(3)]
        if diagonal1.count(tipo) == 2 and Tabuleiro.DESCONHECIDO in diagonal1:
            return (diagonal1.index(Tabuleiro.DESCONHECIDO), diagonal1.index(Tabuleiro.DESCONHECIDO))
        if diagonal2.count(tipo) == 2 and Tabuleiro.DESCONHECIDO in diagonal2:
            return (diagonal2.index(Tabuleiro.DESCONHECIDO), 2 - diagonal2.index(Tabuleiro.DESCONHECIDO))
        return None

    def criar_dupla_sequencia(self) -> (int, int):
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    self.matriz[l][c] = self.tipo
                    duplas = 0
                    if self.verificar_vitoria_ou_bloqueio(self.tipo):
                        duplas += 1
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                    if duplas >= 2:
                        return (l, c)
        return None

    def marcar_canto_oposto(self) -> (int, int):
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto in cantos:
            l, c = canto
            oposto = (2 - l, 2 - c)
            if self.matriz[l][c] == self.oponente and self.matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                return oposto
        return None

    def marcar_canto_vazio(self) -> (int, int):
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto in cantos:
            l, c = canto
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)
        return None

    def marcar_aleatoriamente(self) -> (int, int):
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)
        return None
