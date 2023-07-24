from sistema_2 import Offgrid
import math

class Mixto(Offgrid):
    def __init__(self,consumo,tension,factor,radiacion):
        super().__init__(consumo,15,tension,factor,radiacion)
        self.consumo=consumo
        self.watts=self.calcular_paneles_mixto()

    def calcular_paneles_mixto(self):
        watts_offgrid=self.calcular_watts()
        watts_total=watts_offgrid + self.consumo*self.factor 
        return math.ceil(watts_total)
    
    def cantidad_bateria_mixto(self)->tuple:
        self.calcular_trabajo()
        self.calcular_capacidad()
        cantidad=self.calcular_cantidad()
        capacidad=self.asignar_capacidad()
        return (capacidad,cantidad)

    def obtener_cantidad(self):
        if self.calcular_wp()[0]!= None:
                cantidad=((self.consumo*4)*1.3)/(self.factor*self.watts_pico[0])
                return (math.ceil(cantidad))
        else:
            print("no tenemos sistemas para este consumo")

    def calcular_wp(self)->tuple:
        if self.consumo<1000:
            wp=100
        elif self.consumo<2000:
            wp=300
        elif self.consumo<3000 :
            wp=450
        elif self.consumo>3001:
            return None
        return(wp,self.consumo)



