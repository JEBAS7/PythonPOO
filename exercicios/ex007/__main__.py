from rich import inspect
from classes import Aluno, Professor, Funcionario, Pessoa


def main():
    a1 = Aluno('José', 17, 'Informatica', 'T01')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    #inspect(a1, methods=True)

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
    p1.fazer_aniversario()
    p1.dar_aula()
    #inspect(p1, methods=True)

    f1 = Funcionario('Cláudia', 27, 'Secretária', 'Secretaria')
    f1.fazer_aniversario()
    f1.bater_ponto()
    #inspect(f1, methods=True)

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == '__main__':
    main()
