from provincias import provincias
from sistema_2 import Offgrid
from sistema_1 import Ongrid
from sistema_3 import Mixto
from sistema import *
from angulo import *

while True:
      datos=calcular_angulo(provincias)
      try:
            angulo=datos[1]
            provincia=datos[0]
            factor=datos[2]
            radiacion=datos[3]
            tipo=obtener_tipo()
      except Exception:
            break
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
                  if inversor!=None and datos!=None:
                        print(f"\npara instalar un sistema {tipo} en {provincia} vas a necesitar",
                              f"\n-{cantidad} paneles de {watts_pico} watts (los paneles deben tener una inclinacion",
                              f" de {angulo} mirando al norte) \n-un inversor {tipo} de {inversor} watts") 
            except TypeError:
                  print("no contamos con sistemas para ese consumo")
            except NameError:
                  print("")
      elif tipo=="offgrid":
            try:
                  consumo=int(input("ingrese el consumo de todo lo que desea instalar en el sistema "))
                  tiempo=int(input("ingrese el tiempo que desea utilizarlo (debe ser un numero entero en horas) "))
            except ValueError:
                  print("error. ingresa un numero ")
                  break
            ##### inversor ####
            datos=calcular_inversor(consumo)
            inversor=datos[0]
            tension=int(datos[1])
            sistema=Offgrid(consumo,tiempo,tension,factor,radiacion)
            #### bateria ####
            capacidad=sistema.asignar_capacidad()
            serie=sistema.calcular_cantidad_serie()
            paralelo=sistema.calcular_cantidad_paralelo()
            #### paneles ####
            potencia_panel=sistema.obtener_watts()
            cantidad_pv=sistema.calcular_paneles()
            if capacidad!=None and potencia_panel!=None and paralelo!=1 and serie==1:
                  print(f"\npara instalar un sistema {tipo} en {provincia} vas a necesitar",
                        f"\n- {serie} en serie y {paralelo} en paralelo baterias con una tension de {tension}v y capacidad de {capacidad} AH",
                        f"\n- {cantidad_pv} paneles de {potencia_panel}w (los paneles deben tener una inclinacion",
                        f" de {angulo} mirando al norte)",
                        f"\n- 1 inversor {tipo} de {inversor}w")
            elif paralelo==1 and serie==1:
                  print(f"\npara instalar un sistema {tipo} en {provincia} vas a necesitar",
                        f"\n- {serie} baterias con una tension de {tension}v y capacidad de {capacidad} AH",
                        f"\n- {cantidad_pv} paneles de {potencia_panel}w (los paneles deben tener una inclinacion",
                        f" de {angulo} mirando al norte)",
                        f"\n- 1 inversor {tipo} de {inversor}w")
            else:
                  print("no tenemos sistemas para ese consumo")
      elif tipo =="mixto":
            try:
                  kw=int(input("ingrese los kw consumidos en su ultima boleta de electricidad "))
                  consumo_diario=(kw*1000)/ 30
                  consumo=(kw*1000)/ 720
            except ValueError:
                  print("error. ingresa un numero")
            #### inversor ####
            datos=calcular_inversor(consumo)
            inversor=datos[0]
            tension=int(datos[1])
            sistema=Mixto(consumo,tension,factor,radiacion)
            #### bateria ####
            datos=sistema.cantidad_bateria_mixto()
            capacidad=datos[0]
            serie=datos[1]
            paralelo=datos[2]
            #### paneles ####
            potencia_panel=sistema.calcular_wp()
            cantidad_pv=sistema.obtener_cantidad()
            if capacidad!=None and potencia_panel!=None and paralelo!=1 and serie!=1:
                  print(f"\npara instalar un sistema {tipo} en {provincia} vas a necesitar",
                        f"\n- {serie} en serie y {paralelo} en paralelo baterias con una tension de {tension}v y capacidad de {capacidad} AH",
                        f"\n- {cantidad_pv} paneles de {potencia_panel}w (los paneles deben tener una inclinacion",
                        f" de {angulo} mirando al norte)",
                        f"\n- 1 inversor {tipo} de {inversor}w")
            elif paralelo==1 and serie==1:
                  print(f"\npara instalar un sistema {tipo} en {provincia} vas a necesitar",
                        f"\n- {serie} baterias con una tension de {tension}v y capacidad de {capacidad} AH",
                        f"\n- {cantidad_pv} paneles de {potencia_panel}w (los paneles deben tener una inclinacion",
                        f" de {angulo} mirando al norte)",
                        f"\n- 1 inversor {tipo} de {inversor}w")
            else:
                  print("no tenemos sistemas para ese consumo")