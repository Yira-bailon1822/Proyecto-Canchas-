from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from app.database import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    cancha_id = Column(Integer, ForeignKey("canchas.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    precio_total = Column(Float, nullable=False)
    estado = Column(String(20), default="Confirmada")

    cancha = relationship("Cancha", back_populates="reservas")
    usuario = relationship("Usuario", back_populates="reservas")
