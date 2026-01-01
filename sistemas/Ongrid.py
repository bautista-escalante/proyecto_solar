import math
from servicios.inversor import calcular_inversor

class Ongrid:
    def __init__(self,factor: float,consumo: float, radiacion: float, potencia_panel_wp: int):
        self.factor = factor
        self.consumo = consumo
        self.radiacion = radiacion
        self.potencia_panel_wp = potencia_panel_wp

    def potencia_necesaria_kwp(self) -> float:
        return self.consumo / (self.radiacion * self.factor)

    def cantidad_paneles(self) -> int:
        kwp = self.potencia_necesaria_kwp()
        return math.ceil((kwp * 1000) / self.potencia_panel_wp)

    def inversor_recomendado(self) -> int | None:
        datos = calcular_inversor(self.consumo)
        return datos[0] if datos else None
