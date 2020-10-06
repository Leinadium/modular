# -*- coding: utf-8 -*-
"""
Módulo para operacoes com os peoes.
Peao:
    id: inteiro
    cor: string
"""

peoes = []
id_peao_atual = 0


def limpar_peoes():
    """Limpa todos os peoes salvos. Retorna 0."""
    global id_peao_atual
    peoes.clear()
    id_peao_atual = 0
    return 0


def criar_peao(cor):
    """Cria um peao. Retorna seu id."""
    global id_peao_atual
    peao = dict()

    peao['id'] = id_peao_atual
    id_peao_atual += 1
    peao['cor'] = cor
    peoes.append(peao)
    return peao['id']


def acessar_peao(id_peao):
    """Acessa a cor do peao. '' se nao existir esse id."""
    for p in peoes:
        if p['id'] == id_peao:
            return p['cor']
    return ''


'''
def acessar_peoes(pos=-1, cor='', id_peao=-1):
    """Retorna uma lista dos id dos peoes daquela cor ou na posicao."""
    # copia para nao quebrar o encapsulamento
    if id_peao != -1:
        return [x.copy() for x in peoes if x['id'] == id_peao]
    if pos != -1:
        return [x.copy() for x in peoes if x['pos'] == pos]
    if cor != '':
        return [x.copy() for x in peoes if x['cor'] == cor]

    return []


def atualizar_peao(id_peao, pos, deslocamento):
    """Atualiza posicao do peao. Retorna 0 no sucesso, 1 se não houver peão com aquele id."""
    for p in peoes:
        if p['id'] == id_peao:
            p['pos'] = pos
            p['deslocamento'] += deslocamento
            return 0
    return 1


def reiniciar_peao(id_peao):
    """Recoloca o peao na posicao inicial. Retorna 0 no sucesso, 1 se não houver peao com aquele id."""
    for p in peoes:
        if p['id'] == id_peao:
            p['pos'] = p['pos_inicial']
            p['deslocamento'] = 0
            return 0
    return 0
'''
