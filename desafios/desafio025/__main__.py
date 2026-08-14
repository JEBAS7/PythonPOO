from rich import print
from rich.table import Table
# Substitua pelo nome real do arquivo onde estão suas classes (ex: desafio025 ou logistica)
from transportes import Moto, Caminhao, Drone


def main():
    # Distância configurada igual à do Guanabara
    dist = 100

    # 1. Criando e configurando a tabela da biblioteca rich
    tabela = Table(title="Tabela de Fretes")

    tabela.add_column("Distância", justify="left")
    tabela.add_column("Tipo", justify="left")
    tabela.add_column("Frete", justify="left")

    # 2. Instanciando os objetos de transporte
    transportes = [
        Moto(dist),
        Caminhao(dist),
        Drone(dist)
    ]

    # 3. Varrendo os transportes e adicionando as linhas na tabela
    for t in transportes:
        nome_tipo = t.__class__.__name__

        # Vamos usar um try/except para capturar o erro de limite e exibir o texto correto
        try:
            valor_frete = t.calc_frete()
            string_frete = f"R${valor_frete:.2f}"
        except ValueError as erro:
            # Se disparar o erro do Drone (ou do Caminhão), usamos o texto do erro
            string_frete = str(erro)

        # Adiciona a linha formatada na tabela
        tabela.add_row(f"{dist}Km", nome_tipo, string_frete)

    # 4. Imprime a tabela estilizada na tela
    print(tabela)


if __name__ == "__main__":
    main()
