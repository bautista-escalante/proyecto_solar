import math
class paneles:
    def __init__(self,tipo,factor):
        self.factor=factor
        self.tipo=tipo
        self.consumo= self.calcular_consumo()
        self.watts_pico= self.calcular_wp()

    def calcular_consumo(self)->int:
        if self.tipo=="ongrid":
            kw=int(input("ingrese los kw consumidos en su ultima boleta de electricidad "))
            watts=(kw*1000)/ 720
            return math.ceil(watts)

    def calcular_wp(self)->int:
        if self.consumo<1000:
            wp=100
        elif self.consumo<2000:
            wp=300
        elif self.consumo<3000 :
            wp=450
        elif self.consumo>3001:
            return None
        return wp,self.consumo

    def obtener_cantidad(self):
        if self.watts_pico[0]!= None:
                cantidad=((self.consumo*4)*1.3)/(self.factor*self.watts_pico[0] )
                return (math.ceil(cantidad))
        else:
            print("no tenemos sistemas para este consumo")
            return False,False,False
