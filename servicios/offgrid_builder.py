from core.models.Offgrid import Offgrid
from core.rules.inversor import calcular_inversor

class Offgrid_builder:
      
    @staticmethod
    def construir_sistema_offgrid(consumo, tiempo, factor, radiacion, watts_panel_wp, capacidad_bateria) -> dict:
        
        datos = calcular_inversor(consumo)
        inversor = datos[0]
        tension = int(datos[1])

        sistema = Offgrid(consumo, tiempo, factor, radiacion, watts_panel_wp, capacidad_bateria, tension)

        cantidad_baterias = sistema.calcular_cantidad_baterias()
        serie  = sistema.calcular_cantidad_serie(tension)
        paralelo = sistema.calcular_cantidad_paralelo()
        cantidad_paneles = sistema.calcular_paneles()

        return {
            "paneles": {
                "cantidad": cantidad_paneles,
                "potencia_unitaria_w": sistema.watts_pv,
                "potencia_total_w": cantidad_paneles * sistema.watts_pv
            },
            "inversor": {
                "potencia_w": inversor,
                "tension_v": tension,
                "tipo": "onda pura"
            },
            "bateria": {
                "necesaria": True,
                "cantidad": cantidad_baterias,
                "capacidad_unitaria_ah": capacidad_bateria,
                "configuracion": {
                    "serie": serie,
                    "paralelo": paralelo
                },
                "voltaje_banco": tension
            }
        }