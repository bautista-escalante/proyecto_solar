
def obtener_tipo():
    print("en el mercado existen tres tipos de sistema fotovoltaicos electricos ON-GRID, OFF-GRID y MIXTO \n")
    print("ON-GRID: \nel objetivo principal es reducir el consumo electrico domiciliario. En esta instalacion",
    " se utiliza la energia de los paneles para lo que se usa durante el dia de forma que el exedente se da",
    " a el provedor de electricidad que lo reduce de  la boleta")
    print("OFF-GRID: \nel objetivo principal es tener electricidad ante un corte, En esta intalacion se",
          " utiliza la energia almacenada en baterias previamente cargadas con los paneles")
    print("MIXTO: \nel objetivo principal es consegir el auto-consumo, esta instalacion conbina ambas tecnologias")
    tipo=input("elegi una  ONGRID, OFFGRID o MIXTO ")
    tipo=tipo.lower()
    while tipo!="ongrid" and tipo!="offgrid" and tipo!="mixto" :
        tipo=input("error. elegi una  ONGRID, OFFGRID o MIXTO ")
        tipo=tipo.lower()
    return tipo

def calcular_inversor(consumo):
    if consumo<900:
        return (1000,12)
    elif consumo<1800:
        return (2000,24)
    elif consumo<2700:
        return (3000,48)
    elif consumo>2701:
        return "no tenemos sistemas pera esta cantidad de consumo"




