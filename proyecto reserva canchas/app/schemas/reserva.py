from datetime import datetime
from pydantic import BaseModel, field_validator
from app.schemas.usuario import UsuarioResponse
from app.schemas.cancha import CanchaResponse

class ReservaBase(BaseModel):
    cancha_id: int
    usuario_id: int
    fecha_inicio: datetime
    fecha_fin: datetime

    @field_validator('fecha_fin')
    @classmethod
    def validar_fechas(cls, v, info):
        if 'fecha_inicio' in info.data and v <= info.data['fecha_inicio']:
            raise ValueError('La fecha de fin debe ser posterior a la fecha de inicio')
        return v

class ReservaCreate(ReservaBase):
    pass

class ReservaUpdate(BaseModel):
    fecha_inicio: datetime | None = None
    fecha_fin: datetime | None = None
    estado: str | None = None

class ReservaResponse(BaseModel):
    id: int
    cancha_id: int
    usuario_id: int
    fecha_inicio: datetime
    fecha_fin: datetime
    precio_total: float
    estado: str
    cancha: CanchaResponse | None = None
    usuario: UsuarioResponse | None = None

    class Config:
        from_attributes = True
