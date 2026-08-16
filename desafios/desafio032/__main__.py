from classes032 import ContaBancaria
from rich import print, inspect

def main():
    print("Criando a conta...")
    cc = ContaBancaria(123, "Gustavo", 1000, "Gafanhoto")

    print("Realizando depósito")
    cc.depositar(500)

    print("Realizando saque")
    cc.sacar(200, 'Gafanhoto')

    cc.nome = 'Manuel'

    # Deixei o inspect aqui no final para você conferir o saldo depois das operações!
    inspect(cc, private=True, methods=True)

if __name__ == "__main__":
    main()
