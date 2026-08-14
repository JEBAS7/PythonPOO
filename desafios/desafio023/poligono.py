from abc import ABC, abstractmethod
import math

# --- CLASSE MÃE (ABSTRATA) ---
class Poligono(ABC):
    def __init__(self, qtd_lados: int):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


# --- CLASSE FILHA: QUADRADO ---
class Quadrado(Poligono):
    def __init__(self, lado: float):
        # Um quadrado sempre possui 4 lados
        super().__init__(qtd_lados=4)
        self.lado = lado

    def perimetro(self) -> float:
        return self.lado * 4

    def area(self) -> float:
        return self.lado ** 2


# --- CLASSE FILHA: CÍRCULO ---
class Circulo(Poligono):
    def __init__(self, raio: float):
        # Como o círculo herda de Poligono, definimos a quantidade de lados como 0
        super().__init__(qtd_lados=0)
        self.raio = raio

    def perimetro(self) -> float:
        # O perímetro do círculo é o comprimento da circunferência: 2 * pi * r
        return 2 * math.pi * self.raio

    def area(self) -> float:
        # A área do círculo: pi * r²
        return math.pi * (self.raio ** 2)
