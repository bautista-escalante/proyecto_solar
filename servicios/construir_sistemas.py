from sistemas.Ongrid import Ongrid

def construir_sistema_ongrid(sistema: Ongrid) -> dict:
    cantidad = sistema.cantidad_paneles()
    inversor = sistema.inversor_recomendado()

    return {
        "paneles": {
            "cantidad": cantidad,
            "potencia_unitaria_w": sistema.potencia_panel_wp,
            "potencia_total_w": cantidad * sistema.potencia_panel_wp
        },
        "inversor": {
            "potencia_minima_w": inversor,
            "tipo": "onda pura"
        },
        "bateria": {
            "necesaria": False,
            "capacidad_ah": None,
            "voltaje_banco": None
        }
    }
