from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    activo = Column(Boolean, default=True)

    reservas = relationship("Reserva", back_populates="usuario", cascade="all, delete-orphan")
