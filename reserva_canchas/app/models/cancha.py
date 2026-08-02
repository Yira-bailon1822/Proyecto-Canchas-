from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class CanchaModel(Base):
    __tablename__ = "canchas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo_deporte = Column(String, nullable=False)
    precio_por_hora = Column(Float, nullable=False)
    activa = Column(Boolean, default=True)