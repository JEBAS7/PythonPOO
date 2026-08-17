class Termostato:
    def __init__(self, temperatura_inicial: float = 24.0):
        # Inicializa o atributo privado. Começa em 24.0 por padrão.
        self.__temperatura = 24.0
        # Usamos o setter já na inicialização para garantir as regras de validação
        self.temperatura = temperatura_inicial

    # --- GETTER ---
    @property
    def temperatura(self) -> float:
        """Retorna o valor numérico da temperatura."""
        return self.__temperatura

    # --- SETTER ---
    @temperatura.setter
    def temperatura(self, novo_valor: float):
        """Valida e altera a temperatura respeitando os limites do desafio."""
        # 1. Garante que o valor seja um número flutuante
        novo_valor = float(novo_valor)

        # 2. Regra do Incremento: Arredonda para o 0.5 mais próximo
        # Exemplo: 22.3 vira 22.5 | 22.1 vira 22.0
        novo_valor = round(novo_valor * 2) / 2

        # 3. Regra dos Limites: Mantém o valor entre 16.0 e 30.0
        if novo_valor < 16.0:
            self.__temperatura = 16.0
        elif novo_valor > 30.0:
            self.__temperatura = 30.0
        else:
            self.__temperatura = novo_valor

    # --- GETTER FORMATADO ---
    @property
    def ftemperatura(self) -> str:
        """Retorna a temperatura formatada como texto (ex: '22.5°C')."""
        return f"{self.__temperatura:.1f}°C"
