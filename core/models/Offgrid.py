class Offgrid:
    def __init__(self, consumo, tiempo, factor, radiacion, watts_panel_wp, capacidad_bateria, tension):
        self.consumo = consumo
        self.factor = factor
        self.tiempo = tiempo
        self.radiacion = radiacion
        self.watts_pv = watts_panel_wp
        self.capacidad_bateria = capacidad_bateria
        self.tension = tension 

        # ahora sí se pueden calcular
        self.trabajo = self.calcular_trabajo()
        self.watts = self.calcular_watts_necesarios()
        self.capacidad_necesaria = self.calcular_capacidad_necesaria()

    def calcular_cantidad_serie(self, tension):
        match tension:
            case 12: return 1  
            case 24: return 2
            case 48: return 4
            case _:  return None

    def calcular_cantidad_paralelo(self):
        if self.capacidad_necesaria < 200:   return 1 
        elif self.capacidad_necesaria < 300: return 2
        elif self.capacidad_necesaria < 600: return 3
        else: return None