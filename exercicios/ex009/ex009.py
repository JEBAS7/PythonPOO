class Avaliacao:

    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protected (#)


    # Métodos Acessores
    def get_nota(self): # Método Getter
        return self._nota


    def set_nota(self, nota): # Método Setter
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print('Nota inválida!')