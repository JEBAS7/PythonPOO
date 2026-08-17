from classes029 import Diario
from rich import print, inspect

def main():
    d = Diario('Gafanhoto')

    d.escrever('Primeira mensagem')
    d.escrever('Você é uma pessoa simpática')
    d.escrever(' Você gosta de Python')

    inspect(d, private=True, methods=True)

    # Testando com a senha errada (deve dar Acesso Negado)
    d.ler("SenhaIncorreta")
    d.ler("Gafanhoto")

if __name__ == '__main__':
    main()
