import unittest
import entidades.peao
import entidades.jogador


class TestesJogador(unittest.TestCase):
    def test_limpar_jogadores(self):
        self.assertEqual(entidades.jogador.limpar_jogadores(), 0, 'limpando jogadores')

    def test_criar_jogador(self):
        self.assertEqual(entidades.jogador.criar_jogador('red', []), 0, 'criando jogadores')

    def test_acessar_jogador(self):
        entidades.jogador.limpar_jogadores()
        entidades.jogador.criar_jogador('red', [1, 2, 3])
        self.assertEqual(entidades.jogador.acessar_jogador('red'),
                         {'cor': 'red', 'peoes': [1, 2, 3]}, 'acessando jogador')

        entidades.jogador.criar_jogador('red', [])
        self.assertEqual(entidades.jogador.acessar_jogador('red'), 2, 'dois jogadores iguais')
        self.assertEqual(entidades.jogador.acessar_jogador('vermelho'), 1, 'nenhum jogador')

    def test_jogador_encapsulamento(self):
        entidades.jogador.limpar_jogadores()
        entidades.jogador.criar_jogador('red', [1])
        x = entidades.jogador.acessar_jogador('red')
        x['peoes'].append(2)
        y = entidades.jogador.acessar_jogador('red')
        self.assertNotEqual(x, y, 'encapsulamento jogador')


class TestesPeao(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_limpar_peao(self):
        self.assertEqual(entidades.peao.limpar_peoes(), 0, 'Limpando Peoes')
        entidades.peao.criar_peao('red', 0)
        entidades.peao.limpar_peoes()
        self.assertEqual(entidades.peao.acessar_peoes(pos=0), [], "Limpando Peoes2")

    def test_criar_peao(self):
        x = entidades.peao.criar_peao('red', 0)
        self.assertGreater(x, -1, "Criando Peao")

    def test_acessar_peao_unico(self):
        entidades.peao.limpar_peoes()
        x = entidades.peao.criar_peao('red', 0)
        y = entidades.peao.criar_peao('yellow', 10)
        self.assertIsNotNone(entidades.peao.acessar_peoes(pos=0))
        self.assertIsNotNone(entidades.peao.acessar_peoes('red'))
        self.assertIsNotNone(entidades.peao.acessar_peoes(pos=10))
        self.assertIsNotNone(entidades.peao.acessar_peoes('yellow'))

    def test_atualizar_peao(self):
        entidades.peao.limpar_peoes()
        x = entidades.peao.criar_peao('red', 0)
        self.assertEqual(entidades.peao.atualizar_peao(x, 10), 0)
        a = entidades.peao.acessar_peoes(pos=10)
        self.assertEqual(len(a), 1)
        self.assertEqual(entidades.peao.atualizar_peao(1000, 1000), 1)


if __name__ == '__main__':
    unittest.main()
