from abc import ABC
from datetime import datetime


class Pessoa(ABC):  # Classe Abstrata
    def __init__(self, nome: str, nascimento: int):
        self._nome = str(nome)
        # ⚠️ CRUCIAL: Sem underline para ativar a validação do setter imediatamente!
        self.nascimento = nascimento

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def nascimento(self) -> int:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano: int):
        ano_atual = datetime.now().year
        valor_ano = int(ano)

        # Validação do ano (impede futuro e passado bizarro)
        if valor_ano < 1900 or valor_ano > ano_atual:
            raise ValueError(f"O ano {valor_ano} é inválido! Digite um ano entre 1900 e {ano_atual}.")
        else:
            self._nascimento = valor_ano

    @property
    def idade(self) -> int:
        ano_atual = datetime.now().year
        return ano_atual - self._nascimento


class Aluno(Pessoa):  # Aluno herda de Pessoa
    def __init__(self, nome: str, nascimento: int, curso_inicial: str):
        # Passa o nome e nascimento para a validação da classe mãe (Pessoa)
        super().__init__(nome, nascimento)

        # Lista oficial de cursos permitidos (igual ao vídeo)
        self.cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT', 'PYTHON']

        self._curso = ""
        # ⚠️ CRUCIAL: Sem underline para ativar a validação do curso na entrada!
        self.curso = curso_inicial

    @property
    def curso(self) -> str:
        return self._curso

    @curso.setter
    def curso(self, novo_curso: str):
        curso_formatado = str(novo_curso).strip().upper()

        # Se o curso não estiver na lista de oficiais, o programa TRAVA com erro
        if curso_formatado not in self.cursos_oficiais:
            raise ValueError(f"O Curso {curso_formatado} não está na lista de cursos oficiais.")
        else:
            self._curso = curso_formatado

    def add_curso(self, curso: str):
        curso_formatado = str(curso).strip().upper()
        if curso_formatado not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso_formatado)
