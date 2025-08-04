from util.io import get_generic_content, get_answer_content
from util.message import show_continue_or_end
from util.validation import validate_operation_selected


def show_arithmetic_option():
    operadores = {"Adição": '+', "Subtração": '-', "Multiplicação": '*', "Divisão": '/'}
    print("-------------------------------- menu -----------------------------")
    print("Escolha o tipo de operacao:")
    for chave, valor in operadores.items():
        print(chave, valor)


def operation_request(): # perguntar qual operacao sera feita
    show_arithmetic_option()
    operacao = get_generic_content()
    validate_operation_selected(operacao)
    show_continue_or_end()
    encerrar = get_answer_content().upper()
    if encerrar.__eq__('S'):
        exit()
    # validate_operation_selected(get_generic_content())


def create_menu():
    while True:
        operation_request()
