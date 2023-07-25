import math
class Ongrid:
    def __init__(self,factor):
        self.factor=factor
        self.consumo= self.calcular_consumo()
        self.watts_pico= self.calcular_wp()

    def calcular_consumo(self)->int:
            try:
                kw=int(input("ingrese los kw consumidos en su ultima boleta de electricidad "))
            except ValueError:
                print("error. ingresa un numero ")
                return None
            except UnboundLocalError:
                 print("error. ingresa un numero ")
                 return None
            else:
                watts=(kw*1000)/ 720
                return math.ceil(watts)

    def calcular_wp(self)->int:
        if self.consumo!=None:
            if self.consumo<1000:
                wp=100
            elif self.consumo<2000:
                wp=300
            elif self.consumo<3000 :
                wp=450
            elif self.consumo>3001:
                return None
            return wp,self.consumo
        else:
            print("error")

    def obtener_cantidad(self):
        if self.watts_pico[0]!= None:
                cantidad=((self.consumo*4)*1.3)/(self.factor*self.watts_pico[0])
                return (math.ceil(cantidad))
        else:
            print("no tenemos sistemas para este consumo")
