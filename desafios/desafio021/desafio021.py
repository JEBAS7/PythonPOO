from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True # Toda caneta nasce tampada

    def destampar(self):
        self.tampada = False

    def tampar(self):
        # A ação de tampar não precisa saber a cor, apenas muda o estado
        self.tampada = True

    def escrever(self, texto):
        # Primeiro, checamos se a caneta está tampada
        if self.tampada:
            print("[yellow]⚠️ Não dá para escrever com a caneta tampada![/]")
            return

        # Usamos o self.cor (a cor da própria caneta) para escolher a tag do Rich
        if self.cor == 'azul':
            print(f'[blue]{texto}[/]')
        elif self.cor == 'vermelho':
            print(f'[red]{texto}[/]')
        elif self.cor == 'verde':
            print(f'[green]{texto}[/]')
        else:
            print(texto) # Caso seja outra cor sem formatação especial

    def quebrar_linha(self, quebrar=0):
        print('\n' * quebrar, end='') # O end='' evita que o Python pule uma linha extra além do desejado


# --- TESTE DO CÓDIGO ---
c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

# Destampando as canetas para conseguir escrever
c1.destampar()
c2.destampar()
c3.destampar()

# Agora passamos o TEXTO dentro do método escrever
c1.escrever('Olá, tudo bem?')
c1.quebrar_linha(2)

c2.escrever('Olá, Gafanhoto! ')
c2.quebrar_linha(1)

c3.escrever('Vamos exercitar!')
