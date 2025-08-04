import sys
import time
from util.io import get_generic_content, get_int_number, get_float_number
from util.operacao import adicao, subtracao, multiplicacao, divisao
from util.resultado import result
from util.message import message_operacao, message_tentativas, show_continue_or_end

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


def validate_exit_program():
    print("Nenhuma opção correta foi selecionada")
    sys.exit(0)


def validate_operation_selected(operacao):
    message_operacao(operacao)
    global input1, input2, resultado

    try:
        match operacao:
            case '+':
                input1 = get_int_number()
                input2 = get_int_number()
                resultado = adicao(input1, input2)
            case '-':
                input1 = get_int_number()
                input2 = get_int_number()
                resultado = subtracao(input1, input2)
            case '*':
                input1 = get_int_number()
                input2 = get_int_number()
                resultado = multiplicacao(input1, input2)
            case '/':
                input1 = get_float_number()
                input2 = get_float_number()
                resultado = divisao(input1, input2)
            case '':
                validate_exit_program()
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

    result(f"{resultado}\n")
