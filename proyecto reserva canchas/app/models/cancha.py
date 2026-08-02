from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Cancha(Base):
    __tablename__ = "canchas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo_deporte = Column(String(50), nullable=False)
    precio_por_hora = Column(Float, nullable=False)
    activa = Column(Boolean, default=True)

    reservas = relationship("Reserva", back_populates="cancha", cascade="all, delete-orphan")
