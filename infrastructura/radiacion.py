from infrastructura.cargar_provincias import obtener_provincias

def obtener_por_ubicacion(ubicacion):
    provincias=obtener_provincias()
    for provincia in provincias:
        if provincia["nombre"].lower()==ubicacion:
            factor= provincia["factor"]
            radiacion= provincia["radiacion"]
            break
    return factor, radiacion