import os

from src.util.encerrar import encerrar_programa
from src.util.io import obter_input_num
from src.util.operacao import validar_operador_escolhido


def mostrar_menu():
    operadores = {'+': "Adição", '-': "Subtração", '*': "Multiplicação", '/': "Divisão", "sair": ''}
    print(f"{'=' * 20} MENU {'=' * 20}")
    for i, (chave, valor) in enumerate(operadores.items(), start=1):
        print(f"[{i}] {chave} {valor}")
    return len(operadores)


def menu():
    while True:
        qtd_operacoes = mostrar_menu()
        operacao = obter_input_num("Escolha o tipo de operacao:", minimo=1, maximo=qtd_operacoes)
        if operacao == qtd_operacoes:
            os.system("cls" if os.name == "nt" else "clear")
            encerrar_programa()
        validar_operador_escolhido(operacao)
