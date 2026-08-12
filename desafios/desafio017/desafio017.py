from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f'{self.nome.center(30, ' ')}'
        conteudo += f'{'-' * 30}'
        precof = f'{self.preco:,.2f}'
        conteudo += f'{precof.center(30, '.')}'
        etiqueta = Panel(conteudo, title='Produto', width=34)
        print(etiqueta)



# Seus testes idênticos aos do vídeo
p1 = Produto('iPhone 17 Pro Max', 25_000.85)
p2 = Produto('Notebook Gamer', 8_000.00)

p1.etiqueta()
p2.etiqueta()
