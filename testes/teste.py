import unittest
import jogo.peao
import jogo.jogador


class TestesPeao(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_criacao_peao(self):
        jogo.peao.limpar_peoes()
        x = jogo.peao.criar_peao('amarelo')
        # sera que o peao x tem a cor amarelo?
        self.assertEqual(jogo.peao.acessar_peao(x), 'amarelo')
        self.assertEqual(jogo.peao.acessar_peao(19999), '')

    """
    
    def test_limpar_peao(self):
        self.assertEqual(jogo.peao.limpar_peoes(), 0, 'Limpando Peoes')
        jogo.peao.criar_peao('red', 0)
        jogo.peao.limpar_peoes()
        self.assertEqual(jogo.peao.acessar_peoes(pos=0), [], "Limpando Peoes2")

    def test_criar_peao(self):
        x = jogo.peao.criar_peao('red', 0)
        self.assertGreater(x, -1, "Criando Peao")

    def test_acessar_peao_unico(self):
        jogo.peao.limpar_peoes()
        x = jogo.peao.criar_peao('red', 0)
        y = jogo.peao.criar_peao('yellow', 10)
        self.assertIsNotNone(jogo.peao.acessar_peoes(pos=0))
        self.assertIsNotNone(jogo.peao.acessar_peoes('red'))
        self.assertIsNotNone(jogo.peao.acessar_peoes(pos=10))
        self.assertIsNotNone(jogo.peao.acessar_peoes('yellow'))

    def test_atualizar_peao(self):
        jogo.peao.limpar_peoes()
        x = jogo.peao.criar_peao('red', 0)
        self.assertEqual(jogo.peao.atualizar_peao(x, 10), 0)
        a = jogo.peao.acessar_peoes(pos=10)
        self.assertEqual(len(a), 1)
        self.assertEqual(jogo.peao.atualizar_peao(1000, 1000), 1)
    """


if __name__ == '__main__':
    unittest.main()
