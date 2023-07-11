class Offgrid:
    def __init__(self,consumo,tiempo,tension):
        self.trabajo=self.calcular_trabajo()
        self.consumo=consumo
        self.tiempo=tiempo
        self.tension=tension
        self.capacidad=self.calcular_capacidad()
        self.cantidad=self.calcular_cantidad()

    def calcular_trabajo(self):
        trabajo=self.consumo*self.tiempo 
        return trabajo 

    def calcular_capacidad(self):
        capacidad=self.trabajo/(0.30*self.tension)
        return capacidad

    def asignar_capacidad(self):
        if self.capacidad < 100:
            capacidad=100
        elif self.capacidad < 200:
            capacidad =200
        elif self.capacidad <300:
            capacidad = 150
        return capacidad

    def calcular_cantidad(self):  
        match self.tension:
            case 12:
                cantidad=1
            case 24:
                cantidad=2
            case 48:
                cantidad=4
        return cantidad
    



