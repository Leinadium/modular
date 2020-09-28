# from classes.dado import gera_numero
# from classes.peao import Peao
from unittest.mock import Mock


gera_numero = Mock(return_value=6)


class Jogador:
    dado_atual = None
    vitorioso = False
    peoes_vivos = 4
    peoes_finalizados = 0

    def __init__(self, cor, nome):
        self.nome = nome
        self.cor = cor
        # self.peoes = [Peao(cor) for i in range(4)]

    def rodar_dado(self):
        self.dado_atual = gera_numero()
        if 1 <= self.dado_atual <= 6:
            return 0
        return 1

    def checa_vitoria(self):
        return self.peoes_finalizados == 4

