from rich import inspect
from exercicios.ex009.ex009 import Avaliacao


def main():
    av1 = Avaliacao('Pedro', 'Matemática', 9.5 )
    av1.set_nota(7.4)
    print(f'{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}')
    # inspect(av1, private=True)

if __name__ == '__main__':
    main()
