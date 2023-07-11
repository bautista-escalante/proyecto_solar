"""en este programa se debe pedir al usuario que ingrese su consumo electrico, su ubicacion,
el tipo de instalacion que desea 
realizar todas las operaciones correspondientes a el angulo, la cantidad de paneles, cantidad de baterias 
y tipo de inversor 
validar todas las entradas de informacion 
e informar toda esta informacion en un archivo csv """

from angulo import *
from sistema import obtener_tipo
from consumo import calcular_consumo
from provincias import provincias

datos=calcular_angulo(provincias)
print(datos)
angulo=datos[1]
nombre=datos[0]
factor=datos[2]
tipo=obtener_tipo()
datos=calcular_consumo(tipo,factor)
cantidad=datos[0]
watts_pico=datos[1]
watts=datos[2]
if tipo=="ongrid"and watts!= False:
      print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor superior a {5} watts"
            .format(tipo,nombre,cantidad, watts_pico, angulo,watts)) 
elif tipo=="offgrid":
      print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor superior a {5} watts"
            .format(tipo,nombre,cantidad, watts_pico, angulo,watts)) 
elif tipo=="mixto":
      print("\npara instalar un sistema {0} en {1} vas a necesitar\n-{2} paneles de {3} watts (los paneles deben tener una inclinacion de {4} mirando al norte) \n-un inversor superior a {5} watts"
            .format(tipo,nombre,cantidad, watts_pico, angulo,watts)) 