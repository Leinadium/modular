import unittest
import entidades.peao


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
