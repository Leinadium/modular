# -*- coding: utf-8 -*-
"""
Módulo para operacoes com os peoes.
Cada peao possui um id, uma cor e uma posicao (pos).
"""

peoes = []
id_peao_atual = 0


def limpar_peoes():
    """Limpa todos os peoes salvos. Retorna 0."""
    global id_peao_atual
    peoes.clear()
    id_peao_atual = 0
    return 0


def criar_peao(cor, pos):
    """Cria um peao. Retorna seu id."""
    global id_peao_atual
    peao = dict()

    peao['id'] = id_peao_atual
    id_peao_atual += 1

    peao['pos'] = pos
    peao['cor'] = cor
    peoes.append(peao)
    return peao['id']


def acessar_peoes(pos=-1, cor='', id_peao=-1):
    """Retorna uma lista dos id dos peoes daquela cor ou na posicao."""
    if id_peao != -1:
        return [x for x in peoes if x['id'] == id_peao]
    if pos != -1:
        return [x for x in peoes if x['pos'] == pos]
    if cor != '':
        return [x for x in peoes if x['cor'] == cor]

    return []


def atualizar_peao(id_peao, pos):
    """Atualiza posicao do peao. Retorna 0 no sucesso, 1 se não houver peão com aquele id."""
    for p in peoes:
        if p['id'] == id_peao:
            p['pos'] = pos
            return 0
    return 1
