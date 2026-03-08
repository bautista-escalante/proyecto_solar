
from infrastructura.cargar_provincias import obtener_provincias

def calcular_angulo( ubicacion:str)->float:
    """ calcula el angulo de inclinacion de los paneles segun la ubicacion ingresada """

    provincias= obtener_provincias()
    for provincia in provincias:
        if provincia["nombre"].lower()==ubicacion:
            angulo = abs( provincia["latitud"] -5)
            break
        
    return angulo