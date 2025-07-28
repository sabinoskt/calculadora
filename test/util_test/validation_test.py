import unittest
from util.operacao import adicao, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):

    def test_adicao(self):
        expected_value = 256
        test_adicao_function = adicao(128, 128)
        self.assertEqual(expected_value, test_adicao_function) 

    def test_subtracao(self):
        expected_value = 512
        test_subtracao_function = subtracao(768, 256)
        self.assertEqual(expected_value, test_subtracao_function)

    def test_multiplicacao(self):
        expected_value = 1024
        test_multiplicacao_function = multiplicacao(512, 2)
        self.assertEqual(expected_value, test_multiplicacao_function)

    def test_divisao(self):
        expected_value = 256
        test_divisao_function = divisao(1024, 4)
        self.assertEqual(expected_value, test_divisao_function)