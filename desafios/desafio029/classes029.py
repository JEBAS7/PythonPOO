from rich import print
from rich.console import Console

console = Console()

class Diario:
    def __init__(self, senha_inicial: str):
        # Inicializa a lista de segredos vazia e define a senha (tudo privado)
        self.__segredos = []
        self.__senha = str(senha_inicial.strip())

    def escrever(self, msg: str):
        """Método público para adicionar um segredo. Qualquer um pode escrever!"""
        self.__segredos.append(msg.strip())
        console.print("[green]✓[/green] Segredo guardado a sete chaves no diário!")

    def ler(self, senha: str):
        """Método público para ler os segredos. Exige validação da senha."""
        if senha == self.__senha:
            console.print("\n[bold gold1]📖 LENDO O DIÁRIO SECRETO:[/bold gold1]")
            if not self.__segredos:
                print("[italic gray]O diário está em branco... nenhum segredo ainda.[/italic gray]")
            else:
                for i, segredo in enumerate(self.__segredos, 1):
                    print(f"[bold cyan]{i}.[/bold cyan] {segredo}")
        else:
            console.print("\n[bold red]❌ ACESSO NEGADO![/bold red] Senha incorreta. O diário permanece trancado.")


# --- TESTANDO O DIÁRIO SECRETO ---
if __name__ == "__main__":
    # 1. Criamos o diário e definimos a senha secreta como "1234"
    meu_diario = Diario("1234")

    # 2. Vamos adicionar alguns segredos (qualquer um pode fazer isso)
    meu_diario.escrever("Peguei o último pedaço de bolo da geladeira e botei a culpa no gato.")
    meu_diario.escrever("Ainda não sei usar git perfeitamente, mas estou fingindo bem.")

    # 3. Tentativa de leitura com a SENHA INCORRETA (deve bloquear)
    meu_diario.ler("senha_errada")

    # 4. Tentativa de leitura com a SENHA CORRETA (deve liberar os segredos)
    meu_diario.ler("1234")
