from rich import print, inspect
from poligono import *


def main():
    print("--- Testando o Quadrado ---")
    quad = Quadrado(lado=12)
    print(f"Lados do quadrado: {quad.qtd_lados}")
    print(f"Perímetro: {quad.perimetro()} cm")
    print(f"Área: {quad.area()} cm²")

    print("\n--- Testando o Círculo ---")
    circ = Circulo(raio=20)
    print(f"Lados do círculo: {circ.qtd_lados}")
    print(f"Perímetro (Circunferência): {circ.perimetro():.2f} cm")
    print(f"Área: {circ.area():.2f} cm²")

if __name__ == "__main__":
    main()