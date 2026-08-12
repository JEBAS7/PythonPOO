from rich import print
from rich import inspect

class Funcionario:
    # Atributos de Classe
    empresa = 'Curso em video'

    def __init__(self, nome, setor, cargo):
        # Atibutos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {Funcionario.empresa}.'

c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentacao())
#inspect(c1)

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())
#inspect(c2)

