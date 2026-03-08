from infrastructura.cargar_provincias import obtener_provincias

def obtener_radiacion_por_ubicacion(ubicacion:str)->float:
    """ obtiene la radiacion segun la ubicacion ingresada """
    provincias = obtener_provincias()
    
    if ubicacion in provincias:
        return provincias[ubicacion]["radiacion"]
    
    else:
        raise ValueError("Ubicación no encontrada en las provincias disponibles.")

def obtener_factor_por_ubicacion(ubicacion:str)->float:
    """ obtiene el factor segun la ubicacion ingresada """
    provincias = obtener_provincias()
    
    if ubicacion in provincias:
        return provincias[ubicacion]["factor"]
    
    else:
        raise ValueError("Ubicación no encontrada en las provincias disponibles.")