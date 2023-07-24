import math
class Offgrid:
    def __init__(self,consumo,tiempo,tension,factor,radiacion):
        self.consumo=consumo
        self.factor=factor
        self.tiempo=tiempo
        self.tension=tension
        self.radiacion=radiacion
        self.trabajo=self.calcular_trabajo()
        self.watts=self.calcular_watts()
        self.capacidad=self.calcular_capacidad()
        self.cantidad=self.calcular_cantidad_serie()
        self.watts_pv=self.obtener_watts()
        self.capacidad_aprox=self.asignar_capacidad()

    def calcular_trabajo(self):
        trabajo=self.consumo*self.tiempo 
        return trabajo 

    def calcular_capacidad(self):
        try:
            capacidad=self.trabajo/(0.5 * self.tension)
        except ZeroDivisionError:
            print("error")
        return capacidad

    def asignar_capacidad(self):
        if self.capacidad < 100:
            capacidad=100
        elif self.capacidad < 200:
            capacidad =200
        elif self.capacidad <300:
            capacidad = 150
        elif self.capacidad <600:
            capacidad = 200
        else :
            return None
        return capacidad

    def calcular_cantidad_serie(self):  
        match self.tension:
            case 12:
                cantidad=1
            case 24:
                cantidad=2
            case 48:
                cantidad=4
            case _:
                cantidad=None
        return cantidad 
    
    def calcular_cantidad_paralelo(self):  
        if self.capacidad < 100:
            cantidad=1
        elif self.capacidad < 200:
            cantidad=1
        elif self.capacidad <300:
            cantidad=2
        elif self.capacidad <600:
            cantidad=3
        else :
            return None
        return cantidad

    def calcular_watts(self):
        Watts = self.trabajo * 0.75 / self.radiacion 
        return Watts 
    
    def calcular_paneles(self):
        cantidad=self.watts / self.watts_pv
        return math.ceil(cantidad)

    def obtener_watts(self):
        if self.watts<500 :
            watts=150
        elif self.watts<1000:
            watts=270
        elif self.watts<2000:
            watts=450
        else:
            return None
        return watts