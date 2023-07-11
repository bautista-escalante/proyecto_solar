import re
import math
from sistema import obtener_cantidad

def calcular_consumo(tipo:str,factor)->int:
    if tipo=="ongrid":
        kw=int(input("ingrese los kw consumidos en su ultima boleta de electricidad "))
        watts=(kw*1000)/ 720
        return watts 
"""    elif tipo =="offgrid":
        consumo=int(input("ingrese el consumo de todo lo que desea instalar en el sistema  ingrese 0 cuando quiera parar"))
        while consumo!=0:
            resultado= consumo + 0
            print(resultado)
            consumo=int(input("ingrese el consumo de todo lo que desea instalar en el sistema, ingrese 0 cuando quiera parar"))
        tiempo=input("ingrese el tiempo de tabajo")
        trabajo=resultado * tiempo"""


#def calcular_ah():

def calcular_wp(consumo)->int:
    if consumo<1000:
        wp=100
    elif consumo<2000:
        wp=300
    elif consumo<3000 :
        wp=450
    elif consumo>3001:
        return None
    return wp