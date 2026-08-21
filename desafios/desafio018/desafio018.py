from rich import print
from rich.panel import Panel

class Churrasco:
    # 1. Construtor com os atributos que o Guanabara passou na linha 38
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    # 2. Método que faz os cálculos e exibe o painel
    def analisar(self):
        # Cálculos matemáticos
        carne_total = self.quant * 0.4
        custo_total = carne_total * 82.40
        valor_por_pessoa = custo_total / self.quant

        # Montando o texto formatado com as cores do Rich
        texto = (
            f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\n"
            f"Cada participante comerá 0.4Kg e cada Kg custa R$82.40\n"
            f"Recomendo [blue]comprar {carne_total:.3f}Kg[/] de carne\n"
            f"O custo total será de [green]R${custo_total:.2f}[/]\n"
            f"Cada pessoa pagará [yellow]R${valor_por_pessoa:.2f}[/] para participar."
        )

        # Exibe tudo dentro de um Painel com o título centralizado igual ao do vídeo
        print(Panel(texto, title=self.titulo, title_align="center"))


# Programa Pricipal
c1 = Churrasco(titulo="Churras dos Amigos", quant=15)
c1.analisar()
