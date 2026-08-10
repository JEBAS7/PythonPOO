# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = 'vazio', idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade


    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1


    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'


    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# Declaração de Objetos
g1 = Gafanhoto('Maria', 17)
g1.aniversario()
print(g1)
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method
print(g1.__class__)


# print(g1.__doc__) # DUNDER Attribute
