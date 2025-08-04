from src.util.io import obter_conteudo_generico
from src.util.validation import validar_operador_escolhido


def mostar_opcao_aritmetica():
    operadores = {"Adição": '+', "Subtração": '-', "Multiplicação": '*', "Divisão": '/', "Sair": "S/N"}
    print(f"{'-' * 20} menu {'-' * 20}")
    print("Escolha o tipo de operacao:")
    for chave, valor in operadores.items():
        print(chave, valor)


def operacao_escolhida(): # perguntar qual operacao sera feita
    mostar_opcao_aritmetica()
    operacao = obter_conteudo_generico()
    validar_operador_escolhido(operacao)


def mostrar_menu():
    while True:
        operacao_escolhida()
