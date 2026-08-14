from abc import ABC, abstractmethod
from rich import print

# --- CLASSE MÃE (ABSTRATA) ---
class BebidaQuente(ABC):
    def preparar(self):
        print("[yellow]------ Iniciando o Preparo ------[/]")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("[green]--------- Bebida Pronta ---------[/]")

    def ferver_agua(self):
        print("1.[red] Fervendo água a 100º Celsius.[/]")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


# --- CLASSE FILHA: CAFÉ ---
class Cafe(BebidaQuente):
    def misturar(self):
        print("2. [cyan]Passando água pressurizada pelo pó de café moído.[/]")

    def servir(self):
        print("3. [blue]Servindo em xícara pequena.[/]")


# Se quiser fazer o Chá e Leite com a mesma estética de numeração:
class Cha(BebidaQuente):
    def misturar(self):
        print("2. [cyan]Colocando o sachê de ervas em infusão.[/]")

    def servir(self):
        print("3. [blue]Servindo em xícara grande.[/]")


class Leite(BebidaQuente):
    def misturar(self):
        print("2. [cyan]Misturando o leite em pó na água quente.[/]")

    def servir(self):
        print("3. [blue]Servindo em copo alto.[/]")
