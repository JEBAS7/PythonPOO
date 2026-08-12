from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True   # Toda caneta nasce tampada
        self.carga = 100       # Toda caneta nasce com 100% de carga

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        # 1. Primeira trava: Verificar se está tampada
        if self.tampada:
            print("[yellow]⚠️ Não dá para escrever com a caneta tampada![/]")
            return

        # 2. Segunda trava: Verificar se tem tinta (carga)
        if self.carga <= 0:
            print(f"[red]❌ A caneta {self.cor} está sem tinta! Recarregue para poder escrever.[/]")
            return

        # 3. Executa a escrita aplicando a cor correta
        if self.cor == 'azul':
            print(f'[blue]{texto}[/]')
        elif self.cor == 'vermelho':
            print(f'[red]{texto}[/]')
        elif self.cor == 'verde':
            print(f'[green]{texto}[/]')
        else:
            print(texto)

        # 4. Gasta tinta após escrever (cada frase gasta 20% de carga)
        self.carga -= 20
        print(f"[grey50](Carga restante da caneta {self.cor}: {self.carga}%)[/]")

    def recarregar(self):
        self.carga = 100
        print(f"[cyan]🔄 A caneta {self.cor} foi recarregada com sucesso! (100%)[/]")

    def quebrar_linha(self, quebrar=0):
        print('\n' * quebrar, end='')


# --- TESTE DO SISTEMA DE CARGA ---
c1 = Caneta('azul')
c1.destampar()

# Escrevendo várias vezes para simular o gasto de tinta
c1.escrever("Testando a primeira linha de texto.")
c1.escrever("Segunda linha sendo escrita...")
c1.escrever("Escrevendo mais um pouco.")
c1.escrever("A tinta está quase no fim...")
c1.escrever("Última frase antes de acabar!")

# Esta próxima chamada deve bater na trava e avisar que acabou a tinta
c1.escrever("Essa frase não deve ser impressa porque a tinta acabou.")

c1.quebrar_linha(1)

# Recarregando a caneta para voltar a funcionar
c1.recarregar()
c1.escrever("Agora sim! Escrevendo novamente após a recarga.")
