# -*- coding: utf-8 -*-
"""
Trabalho Ludo - Programação Modular 2020.2
Grupo 1:
    Daniel Guimarães
    Gabriel Galvão
    Guilherme Bizzo
"""

#main

from datetime import date

class Partida:
    
    def __init__(self, ident, hora, vencedor):
        self.ident = ident
        self.hora = date.today()
        self.vencedor = vencedor
        
    