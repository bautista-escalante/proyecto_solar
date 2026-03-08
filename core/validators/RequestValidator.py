from api.schemas.CalculoSolarRequest import CalculoSolarRequest


class RequestValidator:
    
        @staticmethod
        def validar_datos_sistema(data: CalculoSolarRequest):
                if data.tipo not in ["offgrid", "ongrid"]:
                    raise ValueError("Tipo de sistema no válido. Debe ser 'offgrid' u 'ongrid'.")
                
                if data.consumo_watts <= 0:
                    raise ValueError("El consumo en watts debe ser un número positivo.")
                
                if data.watts_panel <= 0:
                    raise ValueError("Los watts por panel deben ser un número positivo.")
                
                if data.tipo == "offgrid" and data.capacidad_elegida <= 0:
                    raise ValueError("La capacidad elegida debe ser un número positivo.")
    
                if data.tipo == "offgrid" and data.tiempo <= 0:
                    raise ValueError("El tiempo de uso diario debe ser un número positivo.")
                
                if not data.provincia or not isinstance(data.provincia, str):
                    raise ValueError("La provincia debe ser una cadena de texto no vacía.") 