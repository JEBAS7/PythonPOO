from classes033 import Aluno
from rich import print, inspect


def main():
    print("[bold blue]👨‍🎓 Cadastrando Aluno...[/bold blue]")

    # 1. Cria o aluno com um curso que JÁ EXISTE na lista padrão
    a = Aluno("Jebass", 1977, "ADS")
    b = Aluno("Raiuga", 1998, "PYTHON")
    # 2. Exercício Extra: Tente adicionar um curso REALMENTE NOVO (Ex: "CYBER")
    # O seu sistema deve incluir "CYBER" dentro da lista 'cursos_oficiais'!
    a.add_curso("CYBER")

    a.add_curso("ADS")

    # 3. Exibe o print da lista para conferir se o novo curso entrou
    print("\n[yellow]Lista de Cursos Atualizada:[/yellow]")
    print(a.cursos_oficiais)

    # 4. O nosso inspect clássico para ver a memória
    print("\n[bold green]🔍 Inspecionando o Objeto Final:[/bold green]")
    inspect(a, private=True, methods=True)
    inspect(b, private=True, methods=True)


if __name__ == "__main__":
    main()
