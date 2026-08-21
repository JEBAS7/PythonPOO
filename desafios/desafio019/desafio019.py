from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1

        # Mensagem inicial
        print(
            f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você agora está na [yellow]página {self.pagina_atual}[/]")

    def avancar_paginas(self, quantidade):
        if self.pagina_atual >= self.paginas:
            print(f":open_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")
            return

        avancou_real = 0

        # Avança de 1 em 1 e imprime em tempo real
        for _ in range(quantidade):
            if self.pagina_atual < self.paginas:
                self.pagina_atual += 1
                avancou_real += 1

                # Imprime a página atual imediatamente na mesma linha
                # Correção da linha 32: removido o argumento inválido 'flush'
                print(f"[grey50]Pág{self.pagina_atual}[/] :arrow_forward: ", end="")
                sleep(0.3)
            else:
                break

                # Após o término do laço, imprime o resumo final na mesma linha e pula para a próxima
        if avancou_real > 0:
            print(
                f"[blue]Você avançou {avancou_real} páginas e agora está na [yellow]página {self.pagina_atual}[/]")

        # Se atingiu o final do livro, avisa na linha de baixo
        if self.pagina_atual == self.paginas:
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")


# --- TESTE DO CÓDIGO ---
l1 = Livro(titulo="10 coisas que aprendi", paginas=20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
