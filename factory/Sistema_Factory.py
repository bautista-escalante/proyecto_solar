from core.models.Ongrid import Ongrid
from core.models.Offgrid import Offgrid
from servicios.ongrid_builder import construir_sistema_ongrid
from servicios.offgrid_builder import Offgrid_builder

from core.rules.angulo import calcular_angulo
from infrastructura.propiedad_Solar import obtener_radiacion_por_ubicacion, obtener_factor_por_ubicacion

class SistemaFactory:
    
    @staticmethod
    def crear_sistema(tipo, consumo, watts_panel, capacidad_elegida, tiempo, ubicacion: str):

        radiacion = obtener_radiacion_por_ubicacion(ubicacion)
        factor = obtener_factor_por_ubicacion(ubicacion)
        angulo = calcular_angulo(ubicacion)

        if tipo == "offgrid":
            off_grid = Offgrid(consumo, tiempo, watts_panel, capacidad_elegida, factor, radiacion)
            return Offgrid_builder.construir_sistema_offgrid(off_grid)
        
        elif tipo == "ongrid":
            on_grid = Ongrid( consumo, watts_panel, factor, radiacion, angulo)
            return construir_sistema_ongrid(on_grid)
