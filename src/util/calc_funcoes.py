from src.util.calculadora import Calculadora
from src.util.io import obter_input_num
from src.util.resultado import resultado

calculadora = Calculadora()


def adicao():
    num1 = obter_input_num("Número:")
    num2 = obter_input_num("Outra número:")
    calculadora.adicao(num1, num2)
    resultado(calculadora.get_resultado())
    calculadora.limpar()


def subtracao():
    num1 = obter_input_num("Número:")
    num2 = obter_input_num("Outra número:")
    calculadora.subtracao(num1, num2)
    resultado(calculadora.get_resultado())
    calculadora.limpar()


def multiplicacao():
    num1 = obter_input_num("Número:")
    num2 = obter_input_num("Outra número:")
    calculadora.multiplicacao(num1, num2)
    resultado(calculadora.get_resultado())
    calculadora.limpar()


def divisao():
    num1 = obter_input_num("Número:")
    num2 = obter_input_num("Outra número:")
    try:
        calculadora.divisao(num1, num2)
        resultado(calculadora.get_resultado())
        calculadora.limpar()
    except ValueError as e:
        print(f"Erro: {e}")
