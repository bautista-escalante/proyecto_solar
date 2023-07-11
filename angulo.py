import re 
import copy

def pedir_ubicacion(lista)->str:
    ubicacion=input("ingrese la provincia en la que reside ")
    if re.match(r"[a-z]+",ubicacion)!=None :
        ubicacion=ubicacion.lower()
        for provincia in lista:
            provincia["nombre"]=provincia["nombre"].lower()
            if re.search(ubicacion,provincia["nombre"]):
                return provincia["nombre"]
    else :
        print("error debe ingresar palabras")

def calcular_angulo(lista:list)->tuple:
    lista_compiada=copy.deepcopy(lista)
    nombre=pedir_ubicacion(lista_compiada)
    for provincias in lista_compiada:
        if provincias["nombre"]==nombre.lower():
            angulo=abs(abs( provincias["latitud"] -10))
            return (nombre,angulo,provincias["factor"])