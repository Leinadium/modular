from entidades import *
from unittest.mock import Mock

LISTA_CORES = ['yellow', 'green', 'red', 'blue']
peoes_cor = dict()

escolher_peao = Mock(return_value=0)


def criar_partida():
    """Inicializa a partida, criando os peoes e jogadores.
        Retorna 0."""
    '''
        peao.limpar_peoes()
        peao.criar_peoes(cor)
        tabuleiro.iniciar_tabuleiro(n)
    '''
    peao.limpar_peoes()
    peoes_cor.clear()
    tabuleiro.iniciar_tabuleiro(len(LISTA_CORES))  # 4 cores

    for cor in LISTA_CORES:
        peoes_cor[cor] = list()
        for i in range(4):
            peoes_cor[cor].append(peao.criar_peao(cor))
        tabuleiro.adicionar_peoes(peoes_cor[cor])

    return 0


def rodada(cor):
    """Faz a rodada. 2 se vitoria, 1 se nao fez nada, 0 se foi sucesso, levanta erro caso erro."""

    # rodando dado
    valor_dado = dado.jogar_dado()
    print("Rodei o dado: %d" % valor_dado)

    # descobrindo os valores possiveis
    lista_peoes = peoes_cor[cor]
    lista_peoes_possiveis = []
    peoes_finalizados = 0
    for p in lista_peoes:
        x = tabuleiro.movimentacao_possivel(p, valor_dado)
        if x == -1:
            raise Exception("IdNaoExiste")
        if x == 0:
            lista_peoes_possiveis.append(p)
        if x == 2:
            # o peao ja foi finalizado
            peoes_finalizados += 1

    print("Movimentos possiveis: %d" % len(lista_peoes_possiveis))
    if not lista_peoes_possiveis:
        return 1

    # escolhendo o peao a mover
    i = escolher_peao(lista_peoes_possiveis)
    peao_pra_mover = lista_peoes_possiveis[i]
    print("Escolhido o peao %d" % i)

    # movendo o peao
    posicao_final = tabuleiro.mover_peao(peao_pra_mover, valor_dado)
    if posicao_final == -1:
        raise Exception("IdNaoExiste2")

    if posicao_final == -2 and peoes_finalizados == 3:  # ja tinha acabado tres e acabou outro agora
        return 2

    print("Peao movido para a posicao %d" % posicao_final)

    # verificar peao comido
    lista_peoes_posicao = tabuleiro.acessar_posicao(posicao_final)
    if lista_peoes_posicao == 0:  # casa protegida, nao come
        return 0

    for p in lista_peoes_posicao:
        cor_p = peao.acessar_peao(p)
        if cor_p == cor:  # se for da mesma cor, esquece
            continue
        else:
            print("Peao comido: %d" % p)
            tabuleiro.reiniciar_peao(p)  # comeu o peao

    return 0


def cor_da_rodada():
    i = 0
    while True:
        yield LISTA_CORES[i]
        i += 1
        if i == len(LISTA_CORES):
            i = 0


def rodar_partida():
    """Cria e joga uma partida. Retorna 0 ao seu final."""

    print("Criando a partida.")
    criar_partida()

    print("Comecando a partida. ")
    g = cor_da_rodada()
    x = -1
    cor = ''
    while x != 2:
        cor = next(g)
        print("Vez do %s" % cor)
        x = rodada(cor)
        print("Resultado da rodada: %d\n" % x)
        # input()

    print("%s ganhou" % cor)
    return 0


rodar_partida()
