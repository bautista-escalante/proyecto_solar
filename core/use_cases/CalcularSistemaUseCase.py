from core.validators.RequestValidator import RequestValidator
from factory.Sistema_Factory import SistemaFactory
from api.schemas.CalculoSolarRequest import CalculoSolarRequest


class CalcularSistemaUseCase: 

    @staticmethod
    def ejecutar(data: CalculoSolarRequest):
        # Validar los datos de entrada
        RequestValidator.validar_datos_sistema(data)
            
        # Construir el sistema solar utilizando la fábrica
        resultado = SistemaFactory.crear_sistema(data)
            
        return resultado
        