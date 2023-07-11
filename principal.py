from angulo import *
from sistema import *
from provincias import provincias
from paneles import paneles

datos=calcular_angulo(provincias)
print(datos)
angulo=datos[1]
nombre=datos[0]
factor=datos[2]
tipo=obtener_tipo()
panel=paneles(tipo,factor)
cantidad=panel.obtener_cantidad()
datos=panel.calcular_wp()
watts_pico=datos[0]
watts=datos[1]
inversor=calcular_inversor(watts)

if tipo=="ongrid"and watts!= False:
      print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor de {5} watts"
            .format(tipo,nombre,cantidad, watts_pico, angulo,inversor)) 
elif tipo=="offgrid" and watts!=False:
      print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{6}baterias de {7}ah \n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor superior a {5} watts"
            .format(tipo,nombre,cantidad, watts_pico, angulo,inversor)) 
elif tipo=="mixto":
      print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor superior a {5} watts"
            .format(tipo,nombre,cantidad, watts_pico, angulo,inversor)) 