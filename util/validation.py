import sys
import time
from util.io import get_generic_content, get_int_number, get_float_number
from util.operacao import adicao, subtracao, multiplicacao, divisao

# TODO Refatorar
# print(f"voce escolheu {operacao}")
# print(f"Voce tem {tentativas} tentativas de {tentativas_permitidas}")

tentativas_permitidas = 3
tentativas = 0

def show_continue_or_end():
    print("Encerrar programa? Y/n")

def validate_number_attempts():
    global tentativas
    global tentativas_permitidas

    if tentativas == tentativas_permitidas:
        raise TypeError("Você ultrapassou a quantidades de tentativas permitidas")

    tentativas += 1

def validate_exit_program():
    show_continue_or_end()
    exitProgram = str(get_generic_content()).upper()
    if exitProgram == "Y":
        sys.exit(0)
    elif exitProgram == "N":
        pass
    else:
        print("Nenhuma opcao correta foi selecionada")
        sys.exit(1)

def result():

    return 

def validate_operation_selected(operacao):
    global input1
    global input2

    try:
        match operacao:
            case "+":
                input1 = get_int_number()
                input2 = get_int_number()
                resultado = result(adicao(input1, input2))
            case "-":
                input1 = get_int_number()
                input2 = get_int_number()
                resultado = result(subtracao(input1, input2))
            case "*":
                input1 = get_int_number()
                input2 = get_int_number()
                resultado = result(multiplicacao(input1, input2))
            case "/":
                input1 = get_float_number()
                input2 = get_float_number()
                resultado = result(divisao(input1, input2))
            case _:
                time.sleep(0.5)
                validate_number_attempts()
                validate_exit_program()
    except TypeError:
        print("Nenhuma opção válida selecionada")
        sys.exit(1)

    # TODO refatorar codigo abaixo
    print(f"\nResultado: {resultado}")

