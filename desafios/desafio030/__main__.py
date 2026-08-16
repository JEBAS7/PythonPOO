from classe030 import Credencial
from rich import print, inspect


def main():
    # 1. Criando a credencial com a senha secreta "Gafanhoto123"
    c = Credencial("Gafanhoto123")

    # 2. Inspecionando o objeto para ver o que ficou guardado na memória
    inspect(c, private=True, methods=True)

    print("\n[bold yellow]--- TESTES DE VALIDAÇÃO ---[/bold yellow]")

    # 3. Testando uma senha errada
    tentativa_1 = "senha_errada"
    if c.validar(tentativa_1):
        print(f"Tentativa '{tentativa_1}': [green]Acesso Liberado![/green]")
    else:
        print(f"Tentativa '{tentativa_1}': [red]Senha Incorreta![/red]")

    # 4. Testando a senha correta
    tentativa_2 = "Gafanhoto123"
    if c.validar(tentativa_2):
        print(f"Tentativa '{tentativa_2}': [green]Acesso Liberado! 🔓[/green]")
    else:
        print(f"Tentativa '{tentativa_2}': [red]Senha Incorreta![/red]")


if __name__ == "__main__":
    main()
