import os
import sys
import time

from src.util.calc_funcoes import adicao, subtracao, multiplicacao, divisao
from src.util.encerrar import nenhuma_opcao_escolhida
from src.util.message import messagem_operacao


def validar_operador_escolhido(operacao):
    messagem_operacao(operacao)
    os.system("cls" if os.name == "nt" else "clear")

    try:
        match operacao:
            case 1:
                adicao()
            case 2:
                subtracao()
            case 3:
                multiplicacao()
            case 4:
                divisao()
            case '':
                nenhuma_opcao_escolhida()
            case _:
                print("Escolha apenas a opção de operação")
                time.sleep(0.5)

    except TypeError:
        print("Nenhuma opção válida selecionada")
        sys.exit(1)
