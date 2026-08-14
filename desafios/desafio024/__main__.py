from cafeteria import *

# --- SIMULANDO A CAFETEIRA (TESTE) ---
def main():
    # Criando as opções de bebidas disponíveis na cafeteira
    cafezinho = Cafe()
    chazinho = Cha()
    leite_quente = Leite()

    # Executando o preparo de cada uma
    cafezinho.preparar()
    chazinho.preparar()
    leite_quente.preparar()

if __name__ == "__main__":
    main()