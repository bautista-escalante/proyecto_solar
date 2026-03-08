from pydantic import BaseModel, Field
from typing import Literal

class CalculoSolarRequest(BaseModel):
    
    provincia: str
    tipo: Literal["ongrid", "offgrid"]
    consumo_watts: int = Field(gt=0)
    watts_panel: int = Field(gt=0)
    capacidad_elegida: Literal[100, 150, 200]
    tiempo: float = Field(gt=0, description="Horas de uso diario")
