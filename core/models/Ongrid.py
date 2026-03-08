import math
from core.rules.inversor import calcular_inversor

class Ongrid:
    factor: float
    consumo: float
    radiacion: float
    potencia_panel_wp: int
    angulo: float

    def __init__(self,consumo: float, potencia_panel_wp: int, factor: float, radiacion: float, angulo: float):
        self.factor = factor
        self.radiacion = radiacion
        self.consumo = consumo
        self.potencia_panel_wp = potencia_panel_wp
        self.angulo = angulo

    def potencia_necesaria_kwp(self) -> float:
        return self.consumo / (self.radiacion * self.factor)

    def cantidad_paneles(self) -> int:
        kwp = self.potencia_necesaria_kwp()
        return math.ceil((kwp * 1000) / self.potencia_panel_wp)

    def inversor_recomendado(self) -> int | None:
        datos = calcular_inversor(self.consumo)
        return datos[0] if datos else None
