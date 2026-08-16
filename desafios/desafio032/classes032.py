import hashlib
from rich import print


class ContaBancaria:
    def __init__(self, id_conta: int, titular: str, saldo_inicial: float, chave: str):
        # Atributos protegidos
        self._id = int(id_conta)
        self._titular = str(titular)

        # Atributos privados
        self.__saldo = float(saldo_inicial) if saldo_inicial >= 0 else 0.0
        self.__hash = ""

        # Define a senha passada por parâmetro (igual à linha 6 do professor)
        self._definir_senha(chave)

        self.cadastrar()

    def cadastrar(self):
        print(f'Conta {self._id} criada com sucesso! Saldo atual R${self.__saldo:.2f}')

    def _definir_senha(self, nova_senha: str):
        texto_bytes = str(nova_senha).encode('utf-8')
        self.__hash = hashlib.sha256(texto_bytes).hexdigest()


    def pede_senha(self) -> str:
        """Pede a senha com asteriscos em tempo real (Windows)."""
        import msvcrt
        import sys
        print("Senha: ", end="", flush=True)
        senha = ""
        while True:
            ch = msvcrt.getch()
            if ch in (b'\r', b'\n'):
                print()
                break
            elif ch == b'\x08':
                if len(senha) > 0:
                    senha = senha[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            else:
                try:
                    senha += ch.decode('utf-8')
                    sys.stdout.write('*')
                    sys.stdout.flush()
                except UnicodeDecodeError:
                    pass
        return senha

    def validar_senha(self, chave: str) -> bool:
        texto_bytes = str(chave).encode('utf-8')
        return hashlib.sha256(texto_bytes).hexdigest() == self.__hash

    def depositar(self, valor: float):
        """Deposita o valor direto no saldo e mostra a mensagem igual ao vídeo."""
        self.__saldo += float(valor)
        # Mensagem idêntica à do Guanabara (usando o self._id)
        print(f"Depósito de R${valor:.2f} autorizado na conta {self._id}")

    def sacar(self, valor: float, chave = ''):
        """Pede a senha de forma segura antes de liberar o saque."""
        # Chame o método de pedir a senha aqui dentro!
        senha_digitada = self.pede_senha()

        if self.validar_senha(senha_digitada):
            if float(valor) <= self.__saldo:
                self.__saldo -= float(valor)
                print(f"[green]✓ Saque de R${valor:.2f} realizado![/green]")
            else:
                print("[red]❌ Saldo insuficiente![/red]")
        else:
            print("[bold red]❌ Senha incorreta! Operação cancelada.[/bold red]")
