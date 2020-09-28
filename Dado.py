# -*- coding: utf-8 -*-
"""
Trabalho Ludo - Programação Modular 2020.2
Grupo 1:
    Daniel Guimarães
    Gabriel Galvão
    Guilherme Bizzo
"""

from random import randint

class Dado:
    
    def __init__(self, valor_atual):
        self.valor_atual = valor_atual

    def gera_numero(self):
        self.valor_atual = randint(1,6)
        return self.valor_atual