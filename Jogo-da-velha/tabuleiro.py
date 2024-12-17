# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]
        ]
        
    def verificar_vencedor(self):
        
        soma_vitoria_x = 3 * Tabuleiro.JOGADOR_X  # 3
        soma_vitoria_0 = 3 * Tabuleiro.JOGADOR_0  # 1 

    
        for linha in self.matriz:
            if sum(linha) == soma_vitoria_x:
                return Tabuleiro.JOGADOR_X
            elif sum(linha) == soma_vitoria_0:
                return Tabuleiro.JOGADOR_0

      
        for col in range(3):
            soma_coluna = sum(self.matriz[row][col] for row in range(3))
            if soma_coluna == soma_vitoria_x:
                return Tabuleiro.JOGADOR_X
            elif soma_coluna == soma_vitoria_0:
                return Tabuleiro.JOGADOR_0

     
        soma_diagonal_principal = sum(self.matriz[i][i] for i in range(3))
        if soma_diagonal_principal == soma_vitoria_x:
            return Tabuleiro.JOGADOR_X
        elif soma_diagonal_principal == soma_vitoria_0:
            return Tabuleiro.JOGADOR_0

    
        soma_diagonal_secundaria = sum(self.matriz[i][2 - i] for i in range(3))
        if soma_diagonal_secundaria == soma_vitoria_x:
            return Tabuleiro.JOGADOR_X
        elif soma_diagonal_secundaria == soma_vitoria_0:
            return Tabuleiro.JOGADOR_0

     
        return Tabuleiro.DESCONHECIDO
