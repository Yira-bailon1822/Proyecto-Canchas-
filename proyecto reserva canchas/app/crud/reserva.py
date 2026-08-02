from sqlalchemy.orm import Session
from app.models.reserva import Reserva
from app.models.cancha import Cancha
from app.models.usuario import Usuario
from app.schemas.reserva import ReservaCreate, ReservaUpdate
from app.exceptions import EntityNotFoundException, BusinessRuleException

def get_reserva(db: Session, reserva_id: int):
    return db.query(Reserva).filter(Reserva.id == reserva_id).first()

def get_reservas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Reserva).offset(skip).limit(limit).all()

def create_reserva(db: Session, reserva: ReservaCreate):
    cancha = db.query(Cancha).filter(Cancha.id == reserva.cancha_id).first()
    if not cancha:
        raise EntityNotFoundException("Cancha", reserva.cancha_id)
    
    usuario = db.query(Usuario).filter(Usuario.id == reserva.usuario_id).first()
    if not usuario:
        raise EntityNotFoundException("Usuario", reserva.usuario_id)

    if not cancha.activa:
        raise BusinessRuleException("No se pueden realizar reservas en una cancha inactiva.")

    if reserva.fecha_inicio.hour < 7 or reserva.fecha_fin.hour > 23 or (reserva.fecha_fin.hour == 23 and reserva.fecha_fin.minute > 0):
        raise BusinessRuleException("El complejo únicamente opera en el horario de 07:00 a 23:00 hs.")

    duracion_horas = (reserva.fecha_fin - reserva.fecha_inicio).total_seconds() / 3600
    if duracion_horas < 1 or duracion_horas > 3:
        raise BusinessRuleException("Las reservas deben tener una duración mínima de 1 hora y máxima de 3 horas.")

    reserva_solapada = db.query(Reserva).filter(
        Reserva.cancha_id == reserva.cancha_id,
        Reserva.estado == "Confirmada",
        Reserva.fecha_inicio < reserva.fecha_fin,
        Reserva.fecha_fin > reserva.fecha_inicio
    ).first()

    if reserva_solapada:
        raise BusinessRuleException("La cancha ya se encuentra reservada en el rango horario seleccionado.")

    precio_total = duracion_horas * cancha.precio_por_hora

    db_reserva = Reserva(
        **reserva.model_dump(),
        precio_total=precio_total
    )
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva

def update_reserva(db: Session, reserva_id: int, reserva: ReservaUpdate):
    db_reserva = get_reserva(db, reserva_id)
    if not db_reserva:
        raise EntityNotFoundException("Reserva", reserva_id)

    update_data = reserva.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_reserva, key, value)

    db.commit()
    db.refresh(db_reserva)
    return db_reserva

def delete_reserva(db: Session, reserva_id: int):
    db_reserva = get_reserva(db, reserva_id)
    if not db_reserva:
        raise EntityNotFoundException("Reserva", reserva_id)
    db.delete(db_reserva)
    db.commit()
    return True
