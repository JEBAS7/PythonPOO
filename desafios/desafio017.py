from rich import print
from rich.table import Table
from rich import box


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        # 1. Criamos a tabela com bordas arredondadas e sem cabeçalho
        tabela = Table(title='Produto', show_header=False, box=box.SQUARE)

        # 2. Definimos uma largura fixa (width) de 32 para a caixa fechar certinho nas pontas
        tabela.add_column(justify="center", width=32)

        # 3. Adiciona o nome do produto
        tabela.add_row(self.nome)

        # 4. A linha do meio do Guanabara: uma string cheia de pontinhos!
        tabela.add_row("------------------------------------------")

        # 5. Formata o preço com a quantidade exata de pontinhos nas laterais
        preco_formatado = f"R${self.preco:,.2f}"

        # Ajustamos os pontos para que caibam perfeitamente na largura 32 da tabela
        if len(preco_formatado) > 9:  # Para o iPhone (R$25,000.85)
            tabela.add_row(f"...........{preco_formatado}...........")
        else:  # Para o Notebook (R$8,000.00)
            tabela.add_row(f"............{preco_formatado}.............")

        print(tabela)
        return tabela


# Seus testes idênticos aos do vídeo
p1 = Produto('iPhone 17 Pro Max', 25_000.85)
p1.etiqueta()

p2 = Produto('Notebook Gamer', 8_000.00)
p2.etiqueta()
