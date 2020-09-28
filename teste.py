from classes.jogador import Jogador
import unittest


class TestesJogador(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_criar_jogador(self):
        jog = Jogador('red', 'teste')
        self.assertEqual(jog.cor, 'red')
        self.assertEqual(jog.nome, 'teste')

    def test_jogador_dado(self):
        jog = Jogador('red', 'teste')
        status = jog.rodar_dado()
        self.assertEqual(status, 0)

    def test_jogador_vitoria_true(self):
        jog = Jogador('red', 'teste')
        jog.peoes_finalizados = 4
        self.assertEqual(jog.checa_vitoria(), True)

    def test_jogador_vitoria_false(self):
        jog = Jogador('red', 'teste')
        jog.peoes_finalizados = 3
        self.assertEqual(jog.checa_vitoria(), False)


if __name__ == '__main__':
    unittest.main()
