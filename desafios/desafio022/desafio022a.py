from rich import print
from rich.table import Table
from rich import box
from rich.console import Console

# Inicializa o console do Rich para limpeza de tela
console = Console()


class ControleRemoto:
    def __init__(self):
        self.canal = 1
        self.volume = 0
        self.ligada = False  # A TV começa desligada

    def passar_canal_frente(self):
        if self.ligada:
            self.canal = 1 if self.canal == 5 else self.canal + 1

    def passar_canal_tras(self):
        if self.ligada:
            self.canal = 5 if self.canal == 1 else self.canal - 1

    def aumentar_volume(self):
        # CORREÇÃO: Agora a trava permite subir até o volume 4!
        if self.ligada and self.volume < 5:
            self.volume += 1

    def diminuir_volume(self):
        if self.ligada and self.volume > 0:
            self.volume -= 1

    def alternar_energia(self):
        self.ligada = not self.ligada

    def status(self):
        # ----------------------------------------------------
        # CASO 1: SE A TV ESTIVER DESLIGADA
        # ----------------------------------------------------
        if not self.ligada:
            tela_tv = Table(title="[ TV ]", show_header=False, box=box.ROUNDED, width=36)
            tela_tv.add_column(justify="center")
            tela_tv.add_row("\n :prohibited: A TV está desligada\n", style="red")
            print(tela_tv)
            print(f" < CH{self.canal} >  -  VOL{self.volume} + ")
            return

        # ----------------------------------------------------
        # CASO 2: SE A TV ESTIVER LIGADA
        # ----------------------------------------------------
        # Aumentamos o width para 36 para caber a barra de volume maior
        tela_tv = Table(title="[ TV ]", show_header=False, box=box.ROUNDED, width=36)
        tela_tv.add_column(justify="left")

        # Linha dos canais
        linha_canais = "CANAL  =  "
        for c in range(1, 6):
            if c == self.canal:
                linha_canais += f"[black on yellow] {c} [/] "
            else:
                linha_canais += f"[grey50]{c}[/] "

        # CORREÇÃO: Barra de volume animada com quadradinhos fixos (MÁXIMO 4)
        barra_volume = "VOLUME =  "
        if self.volume == 0:
            barra_volume += "[grey37]■■■■■[/]"
        elif self.volume == 1:
            barra_volume += "[cyan]■[/][grey37]■■■■[/]"
        elif self.volume == 2:
            barra_volume += "[cyan]■■[/][grey37]■■■[/]"
        elif self.volume == 3:
            barra_volume += "[cyan]■■■[/][grey37]■■[/]"
        elif self.volume == 4:
            barra_volume += "[cyan]■■■■[/][grey37]■[/]"
        elif self.volume == 5:
            barra_volume += "[cyan]■■■■■[/]"

        tela_tv.add_row(linha_canais)
        tela_tv.add_row(barra_volume)
        print(tela_tv)

        print(f" < CH{self.canal} >  -  VOL{self.volume} +")


# =======================================================
# 🚀 MENU INTERATIVO (LAÇO DE REPETIÇÃO DO JOGO)
# =======================================================
meu_controle = ControleRemoto()

while True:
    # Limpa a tela a cada repetição
    console.clear()

    # Mostra o status atual da TV
    meu_controle.status()

    # Captura o comando do usuário
    comando = input("Aperte um botão do controle: ").strip()

    if comando == "+":
        meu_controle.aumentar_volume()
    elif comando == "-":
        meu_controle.diminuir_volume()
    elif comando == ">":
        meu_controle.passar_canal_frente()
    elif comando == "<":
        meu_controle.passar_canal_tras()
    elif comando == "@":
        meu_controle.alternar_energia()
    elif comando == "0":
        print("\n[yellow]Desligando o sistema do controle remoto... Até logo![/]")
        break
    else:
        print("[grey50]Botão inválido! Use +, -, <, >, @ ou 0[/]")

    print('\n' * 10)