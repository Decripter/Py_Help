def subtopicos():
    print(
        """
venv => Criação de ambientes virtuais python
"""
    )


def exibi_ajuda(assunto):
    if assunto == "venv":
        venv()


def venv():
    print(
        """
1 - Crie um ambiente virtual python:

    python3 -m venv venv

2 - Ative o ambiente virtual:

    . venv/bin/activate

* - Para desativar/sair do ambiente virtual:

    deactivate

            """
    )
