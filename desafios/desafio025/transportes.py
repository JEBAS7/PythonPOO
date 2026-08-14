from abc import ABC, abstractmethod


# --- CLASSE MÃE (ABSTRATA) ---
class Transporte(ABC):
    def __init__(self, distancia: float):
        self.distancia = distancia
        self.frete = 0.0

    @abstractmethod
    def calc_frete(self):
        pass


# --- CLASSE FILHA: MOTO ---
class Moto(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 0.50

    def calc_frete(self) -> float:
        # Moto é livre, não precisa de validação de distância
        self.frete = self.distancia * self.fator
        return self.frete


# --- CLASSE FILHA: CAMINHÃO ---
class Caminhao(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 1.20

    def calc_frete(self) -> float:
        # Validação: Mínimo 50Km
        if self.distancia < 50:
            raise ValueError("Caminhão exige uma distância mínima de 50Km.")

        self.frete = self.distancia * self.fator
        return self.frete


# --- CLASSE FILHA: DRONE ---
class Drone(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 9.50

    def calc_frete(self) -> float:
        # Validação: Máximo 10Km
        if self.distancia > 10:
            raise ValueError("Drone possui autonomia máxima de 10Km.")

        self.frete = self.distancia * self.fator
        return self.frete
