from angulo import *
from sistema import *
from provincias import provincias
from sistema_1 import Ongrid
from sistema_2 import Offgrid

datos=calcular_angulo(provincias)
print(datos)
angulo=datos[1]
provincia=datos[0]
factor=datos[2]
tipo=obtener_tipo()
if tipo=="ongrid":
      sistema=Ongrid(factor)
      #### paneles ####
      try:
            cantidad=sistema.obtener_cantidad()
            datos=sistema.calcular_wp()
            watts_pico=datos[0]
            watts=datos[1]
            #### inversor ####
            datos=calcular_inversor(watts)
            inversor=datos[0]
            print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor de {5} watts"
            .format(tipo,provincia,cantidad, watts_pico, angulo,inversor)) 
      except TypeError:
            print("no contamos con sistemas para ese consumo")
elif tipo=="offgrid":
      try:
            consumo=int(input("ingrese el consumo de todo lo que desea instalar en el sistema  ingrese 0 cuando quiera parar"))
            tiempo=int(input("ingrese el tiempo que desea utilizarlo (debe ser un numero entero en horas)"))
      except ValueError:
            print("error. ingresa un numero ")
      ##### inversor ####
      datos=calcular_inversor(consumo)
      inversor=datos[0]
      tension=datos[1]
      sistema=Offgrid(consumo,tiempo,tension)
      #### bateria ####
      capacidad=sistema.asignar_capacidad()
      cantidad=sistema.calcular_cantidad()





"""if tipo=="ongrid"and watts!= False:
      print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor de {5} watts"
            .format(tipo,nombre,cantidad, watts_pico, angulo,inversor)) 
elif tipo=="offgrid" and watts!=False:
      print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{6}baterias de {7}ah \n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor superior a {5} watts"
            .format(tipo,nombre,cantidad, watts_pico, angulo,inversor)) 
elif tipo=="mixto":
      print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor superior a {5} watts"
            .format(tipo,nombre,cantidad, watts_pico, angulo,inversor))""" 