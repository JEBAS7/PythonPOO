import random
from abc import ABC, abstractmethod


# --- CLASSE MÃE (ABSTRATA) ---
class Personagem(ABC):
    def __init__(self, nome: str, vida: int, defesa: int):
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        self.lista_golpes = []

    def atacar(self, alvo: 'Personagem', forca: int):
        from rich import print as rprint
        golpe_sorteado = random.choice(self.lista_golpes)
        rprint(
            f"[green]{self.nome}({self.vida})[/green] atacou [red]{alvo.nome}({alvo.vida})[/red] com um [blue]{golpe_sorteado}[/blue] de força [yellow]{forca}[/yellow]")
        alvo.receber_dano(forca)

    def receber_dano(self, dano_bruto: int):
        from rich import print as rprint
        dano_final = dano_bruto - self.defesa
        if dano_final < 0:
            dano_final = 0

        self.vida -= dano_final
        if self.vida < 0:
            self.vida = 0

        rprint(f"[cyan]{self.nome} recebeu dano de {dano_final}![/cyan]")

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
    def __init__(self, nome: str, vida: int = 2000, defesa: int = 12166):
        super().__init__(nome, vida, defesa)
        self.lista_golpes = ["Golpe de Machado", "Espadada", "Soco"]

    def curar(self):
        from rich import print as rprint
        cura = random.randint(150, 300)
        self.vida += cura
        rprint(f"[blue]{self.nome} fez uma ação de cura e recuperou {cura} pontos de vida.[/blue]")


# --- CLASSE FILHA: MAGO ---
class Mago(Personagem):
    def __init__(self, nome: str, vida: int = 3000, defesa: int = 724):
        super().__init__(nome, vida, defesa)
        self.lista_golpes = ["Bola de Fogo", "Raio Arcano", "Explosão de Gelo"]

    def curar(self):
        from rich import print as rprint
        cura = random.randint(200, 600)
        self.vida += cura
        rprint(f"[blue]{self.nome} fez uma magia de cura e recuperou {cura} pontos de vida.[/blue]")
