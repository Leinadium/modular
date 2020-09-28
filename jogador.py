# from classes.dado import gera_numero
# from classes.peao import Peao
from unittest.mock import Mock


rodar_dado = Mock(return_value=6)


class Jogador:
    dado_atual = None
    vitorioso = False

    def __init__(self, cor, nome):
        self.nome = nome
        self.cor = cor
        # self.peoes = [Peao(cor) for i in range(4)]

    def gera_numero(self):
        self.dado_atual = rodar_dado()
        if 1 <= self.dado_atual <= 6:
            return 0

