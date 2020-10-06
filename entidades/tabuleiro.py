"""
Modulo Tabuleiro.
lista_posicao_iniciais
lista_posicao_seguras
lista_posicao_finais

tabela_peoes:
    id <id> -> id dos peoes
    pos <int> -> posicao atual do peao
    pos_inicial <int> -> posicao original do peao
    eh_finalizado <bool> -> se ja foi até o fim
    eh_inicio <bool> -> esta na origem
"""

# casas normais: 0 .. 13*n - 1

# casas iniciais: 100*i + j
#  i (jogador): 1 .. n, j: 0 .. m

# casas finais: 1000*n + j
#  i (jogador): 1 .. n, j: 0 .. 5 (onde 5 eh a casa final)

# casas seguras: 13*i e 13*i + 8, i: 0 .. 3


N_CORES = 4  # definindo o default do numero de jogadores como 4
N_PEOES = 4  # definindo o default do numero de peoes por jogador como 4
lista_posicao_iniciais = []  # lista de pos do inicio
lista_posicao_seguras = []
lista_posicao_finais = []
tabela_peoes = []
cores_acrescentadas = 0


def _definir_posicoes_iniciais(n, m=N_PEOES):
    global lista_posicao_iniciais
    """Recebe um numero n (ate 9) de jogadores, retorna uma lista de n elementos,
    em que cada elemento eh uma lista das posicoes m das casas iniciais"""
    lista_posicao_iniciais = [[x * 100 + y for y in range(m)] for x in range(1, n + 1)]
    return


def _definir_posicoes_seguras(n):
    """Recebe o numero de jogadores, e retorna a lista de posicoes de casas seguras."""
    global lista_posicao_seguras
    lista_posicao_seguras.clear()
    for i in range(n):
        lista_posicao_seguras.append(13 * i)
        lista_posicao_seguras.append(13 * i + 8)
    return


def _definir_posicoes_finais(n):
    global lista_posicao_finais
    lista_posicao_finais = [1000 * n + 5 for n in range(1, n + 1)]
    return


def iniciar_tabuleiro(n=N_CORES):
    """Recebe o numero de jogadores, e inicia o tabuleiro. Retorna 0."""
    global cores_acrescentadas, N_CORES
    _definir_posicoes_iniciais(n)
    _definir_posicoes_seguras(n)
    _definir_posicoes_finais(n)
    cores_acrescentadas = 0
    N_CORES = n
    return 0


def adicionar_peoes(lista_ids, lista_posicoes=None):
    """Recebe uma lista de peoes e uma lista de posicoes atuais e salva na tabela.
        Retorna 0 se sucesso, 1 se id repitido, 2 se erro."""

    # tamanhos de listas diferentes
    if lista_posicoes is not None and len(lista_ids) != len(lista_posicoes):
        return 2

    # ja acrescentaram todas as cores
    if cores_acrescentadas == N_CORES:
        return 2

    # quantidade de um time diferente de quantidade definida de peoes
    if len(lista_ids) != N_PEOES:
        return 2

    for i, id_peao in enumerate(lista_ids):
        for p in tabela_peoes:
            if id_peao == p['id']:
                return 1

        d = dict()
        d['id'] = id_peao
        d['pos_inicial'] = lista_posicao_iniciais[cores_acrescentadas][i]
        if lista_posicoes is not None:
            d['pos'] = lista_posicoes[i]
            d['eh_finalizado'] = lista_posicoes[i] in lista_posicao_finais
            d['eh_inicio'] = lista_posicoes[i] in lista_posicao_iniciais
        else:
            d['pos'] = d['pos_inicial']
            d['eh_finalizado'] = False
            d['eh_inicio'] = True

        tabela_peoes.append(d)

    return 0


def acessar_posicao(pos):
    """Retorna o id do peao na posicao, 0 se vazio, 1 se protegida, 2 ou mais se tiver mais de um"""
    if pos in lista_posicao_seguras:
        return 1

    r = []
    for p in tabela_peoes:
        if p['pos'] == pos:
            r.append(p['id'])

    if len(r) == 1:
        return r[0]  # retorna o id daquela posicao

    return len(r)  # 0 se vazia, >=2 se mais de um


def reiniciar_peao(id_peao):
    """Realoca o peao para a posicao inicial, reiniciando seus dados.
    0 se sucesso, -1 se nao houver esse id. """
    for p in tabela_peoes:
        if p['id'] == id_peao:
            p['pos'] = p['pos_inicial']
            p['eh_finalizado'] = False
            p['eh_inicio'] = True
            return 0

    return -1

# TODO: criar movimentacao_possivel(id, mov): int
