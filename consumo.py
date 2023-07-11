import re
import math

def calcular_consumo(tipo:str,factor)->tuple:
    if tipo=="ongrid":
        kw=int(input("ingrese los kw consumidos en su ultima boleta de electricidad "))
        watts=(kw*1000)/ 720
        wp=calcular_wp(watts)
        if wp!= None:
            cantidad=((watts*4)*1.3)/(factor*wp )
            return (math.ceil(cantidad),wp,math.ceil(watts))
        else:
            print("no tenemos sistemas para este consumo")
            return False,False,False
    elif tipo =="offgrid":
        input("ingrese el consumo de todo lo que desea instalar en el sistema")
        input("ingrese el tiempo de tabajo")

def calcular_wp(consumo)->int:
    if consumo<1000:
        wp=100
    elif consumo<2000 and consumo>1001:
        wp=300
    elif consumo<3000 and consumo>2001:
        wp=450
    elif consumo>3001:
        return None
    return wp