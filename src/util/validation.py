import sys
import time

from src.util.encerrar import encerrar_programa, nenhuma_opcao_escolhida
from src.util.io import obter_numero_int, obter_numero_float
from src.util.message import messagem_operacao
from src.util.operacao import adicao, multiplicacao, divisao, subtracao
from src.util.resultado import resultar


# tentativas_permitidas = 3
# tentativas = 0


# def validate_number_attempts():
#     global tentativas
#     global tentativas_permitidas
#
#     if tentativas == tentativas_permitidas:
#         raise TypeError("Você ultrapassou a quantidades de tentativas permitidas")
#
#     tentativas += 1
#
#     message_tentativas(tentativas, tentativas_permitidas)


num1, num2, resultado = 0, 0, 0


def validar_operador_escolhido(operacao):
    messagem_operacao(operacao)
    global num1, num2, resultado

    try:
        match operacao:
            case '+':
                num1 = obter_numero_int()
                num2 = obter_numero_int()
                resultado = adicao(num1, num2)
            case '-':
                num1 = obter_numero_int()
                num2 = obter_numero_int()
                resultado = subtracao(num1, num2)
            case '*':
                num1 = obter_numero_int()
                num2 = obter_numero_int()
                resultado = multiplicacao(num1, num2)
            case '/':
                num1 = obter_numero_float()
                num2 = obter_numero_float()
                resultado = divisao(num1, num2)
            case '':
                nenhuma_opcao_escolhida()
            case 'S':
                encerrar_programa()
            case _:
                print("Escolha apenas a opção de operação")
                time.sleep(0.5)
                # validate_operation_selected(get_generic_content())
                # validate_number_attempts()
            # validate_exit_program()
    except TypeError:
        print("Nenhuma opção válida selecionada")
        sys.exit(1)
    except ZeroDivisionError:
        print("Não é possível dividir por zero")

    resultar(f"{resultado}\n")
