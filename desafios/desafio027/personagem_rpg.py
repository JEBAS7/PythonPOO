import random
from rich import print
from abc import ABC, abstractmethod


# --- CLASSE MÃE (ABSTRATA) ---
class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f"[green]{self.nome}({self.vida})[/green] atacou [red]{alvo.nome}({alvo.vida})[/red] com um [blue]{golpe}[/blue] de força [yellow]{forca}[/yellow]")
            alvo.receber_dano(forca)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer')

    def receber_dano(self, dano):
        from rich import print as rprint
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0

        rprint(f"[cyan]{self.nome} recebeu dano de {fator}![/cyan]")

    # === NOVO MÉTODO COMPLEMENTAR (DESAFIO 027) ===
    def morreu(self, personagem_alvo: 'Personagem', reviveu: int = 0):
        """
        Método para verificar morte ou aplicar mecânica de ressurreição.
        reviveu=0 torna o parâmetro opcional no código principal.
        """
        from rich import print as rprint

        # Se um valor de ressurreição foi passado (maior que zero)
        if reviveu > 0:
            personagem_alvo.vida = reviveu
            rprint(
                f"[yellow]✨ {personagem_alvo.nome} usou uma habilidade especial e reviveu com {reviveu} de vida![/yellow]")
        else:
            rprint(f"[red]💀 {personagem_alvo.nome} foi derrotado em combate.[/red]")

    @abstractmethod
    def curar(self):
        pass


# --- CLASSE FILHA: GUERREIRO ---
class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Golpe de Machado", "Espadada", "Soco"]

    def curar(self):
        from rich import print as rprint
        cura = random.randint(150, 300)
        self.vida += cura
        rprint(f"[blue]{self.nome} fez uma ação de cura e recuperou {cura} pontos de vida.[/blue]")


# --- CLASSE FILHA: MAGO ---
class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio Arcano", "Explosão de Gelo"]

    def curar(self):
        from rich import print as rprint
        cura = random.randint(200, 800)
        self.vida += cura
        rprint(f"[blue]{self.nome} fez uma magia de cura e recuperou {cura} pontos de vida.[/blue]")
