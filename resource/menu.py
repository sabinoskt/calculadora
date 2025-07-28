from util.io import get_generic_content
from util.validation import validate_operation_selected


def show_arithmetic_option():
    print("-------------------------------- menu -----------------------------")
    print("Escolha o tipo de operacao:")
    print(" + ")
    print(" - ")
    print(" * ")
    print(" / ")


def operation_request(): # perguntar qual operacao sera feita
    show_arithmetic_option()
    operacao = get_generic_content()
    validate_operation_selected(operacao)


def create_menu():
    operation_request()
