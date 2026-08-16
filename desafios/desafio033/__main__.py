from classes033 import Aluno
from rich import print, inspect


def main():
    print("[bold blue]👨‍🎓 Cadastrando Aluno...[/bold blue]")
    # Criando a Maria no curso de ADS (que é válido!)
    aluno = Aluno("Maria", 2010, "ADM")

    # Mostra o inspect idêntico ao do Guanabara na sua imagem
    inspect(aluno, private=True, methods=True)

    # TESTE DE VALIDAÇÃO: Descomente a linha abaixo se quiser ver o sistema travar caso digite um curso errado:
    # aluno.curso = "Medicina"


if __name__ == "__main__":
    main()
