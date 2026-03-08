from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from api.schemas.CalculoSolarRequest import CalculoSolarRequest
from core.use_cases.CalcularSistemaUseCase import CalcularSistemaUseCase

router = APIRouter()

@router.post("/calculo")
def calcular_sistema(data: CalculoSolarRequest):
    try:
        resultado = CalcularSistemaUseCase.ejecutar(data)
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=resultado)

    except ValueError as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": str(e)})

    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": "Error interno del servidor"})