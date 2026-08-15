class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id # público (+)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        print(f'\033[1;32mConta {self.id} criado com sucesso. Saldo atual de R${self.__saldo:,.2f}.\033[m')

    def __str__(self):
       # return f'\033[1;32mA conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo.\033[m'
        return f'Estado atual da conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'\033[1;34mDepósito de R${valor:,.2f} autorizado na conta {self.id}.\033[m')

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'\033[1;31mSaque NEGADO de R${valor:,.2f} para o conta {self.id}. SALDO INSUFICIENTE\033[m')
        else:
            self.__saldo -= valor
            print(f'\033[1;32mSaque de R${valor:,.2f} autorizado na conta {self.id}.\033[m')
