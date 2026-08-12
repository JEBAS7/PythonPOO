from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []  # Começa como uma lista vazia

    def add_favoritos(self, jogo):
        # Adiciona o jogo na lista de favoritos
        self.favoritos.append(jogo)

    def ficha(self):
        # 1. Organiza a lista de jogos em ordem alfabética (A-Z)
        self.favoritos.sort()

        # 2. Cria o texto de dentro da caixinha
        texto = f"Nome real: [black on blue]{self.nome}[/]\n"
        texto += "Jogos favoritos:\n"

        # 3. Passa por cada jogo da lista e adiciona o emoji de controle 🎮
        for jogo in self.favoritos:
            texto += f":video_game: [blue]{jogo}[/]\n"

        # 4. Desenha o painel com o nick do jogador no título
        print(Panel(texto, title=f"Jogador <{self.nick}>", width=40))


# --- TESTE DO CÓDIGO (Igualzinho ao do Guanabara na imagem) ---
j1 = Gamer(nome="Fabricio da Silva", nick="detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer(nome="Olivia Souza", nick="peach_raivosa")
j2.add_favoritos("Mario Bros.")
j2.add_favoritos("Call of Duty")
j2.ficha()
