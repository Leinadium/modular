"""
Módulo para operacoes com Jogadores.
Cada Jogador possui um id (cor), e uma lista de peões
"""


# lista de jogadores
jogadores = []


def limpar_jogadores():
    """Limpa os jogadores. Retorna 0."""
    jogadores.clear()
    return 0


def criar_jogador(cor, peoes):
    """Cria um jogador com id = cor, e uma lista de peoes. Retorna 0."""
    jog = dict()
    jog['cor'] = cor
    jog['peoes'] = peoes
    jogadores.append(jog)
    return 0


def acessar_jogador(cor):
    """Retorna o jogador daquela cor, 1 se nao houver jogador daquela cor,
    ou 2 se houver mais de um jogador com aquela cor."""

    x = [x for x in jogadores if x['cor'] == cor]
    if len(x) == 0:
        return 1
    if len(x) >= 2:
        return 2

    # retorna uma copia para continuar o encapsulamento
    r = x[0].copy()
    r['peoes'] = x[0]['peoes'].copy()
    return r
