from rich import print


class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1  # Todo livro começa na página 1 ao ser aberto

        # Mensagem inicial idêntica ao vídeo
        print(
            f"[blue]:blue_square: Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você agora está na [yellow]página {self.pagina_atual}[/]")

    def avancar_paginas(self, quantidade):
        # Se o leitor já chegou ao fim, não faz nada
        if self.pagina_atual >= self.paginas:
            print(f"[red]:red_square: Você chegou ao final do livro '{self.titulo}'[/]")
            return

        paginas_impressas = []
        avançou_real = 0

        # Avança de 1 em 1 página até atingir a quantidade solicitada ou o fim do livro
        for _ in range(quantidade):
            if self.pagina_atual < self.paginas:
                self.pagina_atual += 1
                paginas_impressas.append(f"Pág{self.pagina_atual}")
                avançou_real += 1
            else:
                break  # Para o laço se bater no teto de páginas

        # Junta as páginas com a setinha '▶' se alguma página foi percorrida
        if paginas_impressas:
            resultado_paginas = " ▶ ".join(paginas_impressas)
            print(
                f"[grey50]{resultado_paginas}[/] ▶ [blue]Você avançou {avançou_real} páginas e agora está na [yellow]página {self.pagina_atual}[/]")

        # Se após o avanço a página atual for o limite máximo, avisa que acabou
        if self.pagina_atual == self.paginas:
            print(f"[red]:red_square: Você chegou ao final do livro '{self.titulo}'[/]")


# --- TESTE DO CÓDIGO (Igualzinho às linhas 28-31 da sua imagem) ---
l1 = Livro(titulo="10 coisas que aprendi", paginas=20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
