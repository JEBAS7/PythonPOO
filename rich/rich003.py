from rich import print
from rich.table import Table

tabela = Table(title='Tabela de preços')

tabela.add_column('Nome', justify='center', style='bold red')
tabela.add_column('Preço', justify='center', style='bold blue')
tabela.add_row('Lápis', 'R$1,50')
tabela.add_row('Borracha', '[green]R$5,00[/]')

print(tabela)