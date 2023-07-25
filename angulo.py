import re 
import copy

def pedir_ubicacion(lista)->str:
    try:
        ubicacion=input("ingrese la provincia en la que reside ")
        ubicacion=ubicacion.lower()
        for provincia in lista:
            prov=provincia["nombre"].lower()
            if re.findall(ubicacion , prov):
                    return prov
        else:
            print("error. esta provincia no existe")    
    except Exception:
        print("error. ingresa letras")

def calcular_angulo(lista:list)->tuple:
    lista_compiada=copy.deepcopy(lista)
    nombre=pedir_ubicacion(lista_compiada)
    for provincias in lista_compiada:
        if provincias["nombre"].lower()==nombre:
            angulo=abs(abs( provincias["latitud"] -10))
            return (nombre,angulo,provincias["factor"],provincias["radiacion"])
    