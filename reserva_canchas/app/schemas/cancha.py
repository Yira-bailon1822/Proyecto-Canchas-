from pydantic import BaseModel
from typing import Optional

class CanchaBase(BaseModel):
    nombre: str
    tipo_deporte: str
    precio_por_hora: float
    activa: Optional[bool] = True

class CanchaCreate(CanchaBase):
    pass

class CanchaResponse(CanchaBase):
    id: int

    class Config:
        from_attributes = True