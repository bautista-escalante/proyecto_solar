
from infrastructura.cargar_provincias import obtener_provincias

def calcular_angulo(self, ubicacion:str)->float:
    """ calcula el angulo de inclinacion de los paneles segun la ubicacion ingresada """

    provincias= self.obtener_provincias()
    for provincia in provincias:
        if provincia["nombre"].lower()==ubicacion:
            angulo = abs( provincia["latitud"] -5)
            break
    return angulo