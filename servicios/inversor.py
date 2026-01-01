def calcular_inversor(consumo):
    """ calcula la potencia y la tension del inversor segun el consumo ingresado """
    if consumo<900:
        return (1000,12)
    elif consumo<1800:
        return (2000,24)
    elif consumo<2700:
        return (3000,48)
    elif consumo>2701:
        return None