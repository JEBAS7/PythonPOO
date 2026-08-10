from rich import print
from rich import inspect

# print(int)
# inspect(int, all=True)

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'\033[1;32mConta {self.id} criado com sucesso. Saldo atual de R${self.saldo:,.2f}.\033[m')

    def __str__(self):
        return f'\033[1;32mA conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.\033[m'


    def depositar(self, valor):
        self.saldo += valor
        print(f'\033[1;34mDepósito de R${valor:,.2f} autorizado na conta {self.id}.\033[m')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'\033[1;31mSaque NEGADO de R${valor:,.2f} para o conta {self.id}. SALDO INSUFICIENTE\033[m')
        else:
            self.saldo -= valor
            print(f'\033[1;32mSaque de R${valor:,.2f} autorizado na conta {self.id}.\033[m')



c1 = ContaBancaria(112, 'Gustavo', 3000)
inspect(c1)


