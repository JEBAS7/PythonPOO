from classes031 import Retangulo
from rich import print, inspect

def main():
    print("[bold blue]📐 CRIANDO UM RETÂNGULO INICIAL (10 x 5)[/bold blue]")
    r = Retangulo(10, 5)
    print(f'{r.medidas} = {r.area}')
    inspect(r, private=True, methods=True)

    print("\n[bold yellow]🔄 ALTERANDO APENAS A ALTURA PARA 8...[/bold yellow]")
    r.altura = 8
    print(f'{r.medidas} = {r.area}')


    # A área deve mudar automaticamente de 50 para 80!
    inspect(r, private=True, methods=True)

    print("\n[bold green]🚀 ALTERANDO AMBAS AS MEDIDAS DE UMA VEZ COM @medidas = (4, 3)...[/bold green]")
    r.medidas = (4, 3)
    print(f'{r.medidas} = {r.area}')
    # A área deve mudar automaticamente para 12!
    inspect(r, private=True, methods=True)

if __name__ == "__main__":
    main()
