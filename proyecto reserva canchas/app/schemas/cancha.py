from pydantic import BaseModel

class CanchaBase(BaseModel):
    nombre: str
    tipo_deporte: str
    precio_por_hora: float
    activa: bool = True

class CanchaCreate(CanchaBase):
    pass

class CanchaUpdate(BaseModel):
    nombre: str | None = None
    tipo_deporte: str | None = None
    precio_por_hora: float | None = None
    activa: bool | None = None

class CanchaResponse(CanchaBase):
    id: int

    class Config:
        from_attributes = True
