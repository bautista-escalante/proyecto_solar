class SistemaFactory:

    @staticmethod
    def crear_sistema(tipo, datos):
        if tipo == "aislado":
            return sistema_offgrid(datos)
        elif tipo == "red":
            return SistemaConectadoRed(datos)
        elif tipo == "hibrido":
            return SistemaHibrido(datos)
        else:
            raise ValueError("Tipo de sistema no válido")
