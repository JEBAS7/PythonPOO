class Retangulo:
    def __init__(self, base: float, altura: float):
        # Inicializa os atributos protegidos (com apenas um underline)
        self._base = float(base)
        self._altura = float(altura)
        # Calcula a área inicial
        self._recalcular_area()

    def _recalcular_area(self):
        """Método interno (protegido) para manter a área sempre atualizada."""
        self._area = self._base * self._altura

    # --- PROPRIEDADE BASE ---
    # --- GETTER (Deixa ele limpo, apenas retornando o valor numérico) ---
    @property
    def base(self) -> float:
        return self._base

    def __init__(self, base: float, altura: float):
        # 1. Você entrega o valor para o PORTEIRO
        self.base = base
        self.altura = altura

    @base.setter
    def base(self, novo_valor: float):
        # 2. O PORTEIRO inspeciona o valor
        if novo_valor < 0:
            raise ValueError("Não pode ser negativo!")
        else:
            # 3. Se estiver tudo bem, o PORTEIRO guarda no COFRE (_base)
            self._base = float(novo_valor)

    # --- PROPRIEDADE ALTURA ---
    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, novo_valor: float):
        valor_float = float(novo_valor)
        if valor_float < 0:
            raise ValueError("Não pode ser negativo!")
        else:
            # ESSA LINHA É CRUCIAL: cria a variável com underline
            self._altura = valor_float
        self._recalcular_area()

    # --- PROPRIEDADE MEDIDAS (Base e Altura juntas) ---
    @property
    def medidas(self) -> tuple:
        """Retorna uma tupla com (base, altura)."""
        return (self._base, self._altura)

    @medidas.setter
    def medidas(self, novas_medidas: tuple or list):
        """Permite alterar ambas as medidas de uma vez só. Ex: r.medidas = (10, 5)"""
        if len(novas_medidas) == 2:
            self._base = float(novas_medidas[0])
            self._altura = float(novas_medidas[1])
            self._recalcular_area()
            return f'Base: {self._base} \nAltura: {self._altura} \nÁrea: {self._area}'
        else:
            raise ValueError("A tupla de medidas deve conter exatamente 2 valores: (base, altura)")

    # --- PROPRIEDADE ÁREA (Apenas leitura) ---
    @property
    def area(self) -> float:
        """Retorna a área calculada. Não possui setter para não ser burlada!"""
        self._area = self._base * self._altura
        return self._area
