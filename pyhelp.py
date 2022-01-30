#!/usr/local/bin/python3
import sys
from topics import python


def inicio():
    print(
        """
Este é um programa de ajuda.
Os seguintes tópicos estão disponíveis:
"""
    )
    topicos()


def topicos():
    print(
        """
python
"""
    )


def opcao_invalida(nome_opcao):
    print(nome_opcao, " - Este tópico ainda não está disponível.")
    print("Verifique a lista de tópicos disponíveis:")
    topicos()


def main(argumentos):
    if len(argumentos) > 0:
        if argumentos[1] == "python":
            if len(argumentos) > 2:
                python.exibi_ajuda(argumentos[2])
            else:
                python.subtopicos()
        else:
            opcao_invalida(argumentos[1])

    else:
        inicio()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
