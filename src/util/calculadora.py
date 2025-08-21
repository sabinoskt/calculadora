class Calculadora:
    def __init__(self):
       self._resultado = 0

    def get_resultado(self):
        return self._resultado

    def limpar(self):
        self._resultado = 0

    def adicao(self, num1: float, num2: float) -> float:
        self._resultado = num1 + num2
        return self._resultado

    def subtracao(self, num1: float, num2: float) -> float:
        self._resultado = num1 - num2
        return self._resultado

    def multiplicacao(self, num1: float, num2: float) -> float:
        self._resultado = num1 * num2
        return self._resultado

    def divisao(self, num1: float, num2: float) -> float:
        if num2 == 0:
            raise ValueError("Divisão por zero não é permitida")

        self._resultado = num1 / num2
        return self._resultado
