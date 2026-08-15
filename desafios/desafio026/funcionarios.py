from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


# --- CLASSE MÃE (ABSTRATA) ---
class Funcionario(ABC):
    def __init__(self, nome: str, salario_bruto: float = 0.0):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = 0.0
        self.sal_min = 1612.0
        self.inss = 7.5

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        # Desconto do INSS (7.5%)
        desconto = self.salario_bruto * (self.inss / 100)
        self.salario = self.salario_bruto - desconto

        # Proporção em salários mínimos
        qtd_sal_min = self.salario / self.sal_min

        # Monta a string exatamente igual ao print do Guanabara
        nome_classe = self.__class__.__name__
        texto = f'O salário de [blue]{self.nome}[/] ([magenta]{nome_classe}[/magenta]) é de ' f'[green]R${self.salario:.2f}[/green] e corresponde a '  f'[yellow]{qtd_sal_min:.1f} salários mínimos.[/yellow]'

        # Cria o painel estilizado com bordas arredondadas
        painel = Panel(texto, title="Análise de Salário", width=50)

        # Importação local do print do rich para não chocar com o print padrão
        print(painel)


# --- CLASSE FILHA: HORISTA ---
class FuncionarioHorista(Funcionario):
    def __init__(self, nome: str, valor_hora: float, horas_trab: float):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calcular_salario(self):
        self.salario_bruto = self.valor_hora * self.horas_trab


# --- CLASSE FILHA: MENSALISTA ---
class FuncionarioMensalista(Funcionario):
    def __init__(self, nome: str, salario_bruto: float):
        # O mensalista já recebe o salário bruto direto no construtor
        super().__init__(nome, salario_bruto)

    def calcular_salario(self):
        # O salário bruto já está definido, método necessário para cumprir o contrato abstrato
        pass
