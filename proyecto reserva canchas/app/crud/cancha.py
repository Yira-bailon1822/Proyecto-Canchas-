from sqlalchemy.orm import Session
from app.models.cancha import Cancha
from app.schemas.cancha import CanchaCreate, CanchaUpdate

def get_cancha(db: Session, cancha_id: int):
    return db.query(Cancha).filter(Cancha.id == cancha_id).first()

def get_canchas(db: Session, tipo_deporte: str | None = None, activa: bool | None = None, precio_maximo: float | None = None, skip: int = 0, limit: int = 100):
    query = db.query(Cancha)
    if tipo_deporte:
        query = query.filter(Cancha.tipo_deporte.ilike(f"%{tipo_deporte}%"))
    if activa is not None:
        query = query.filter(Cancha.activa == activa)
    if precio_maximo is not None:
        query = query.filter(Cancha.precio_por_hora <= precio_maximo)
    return query.offset(skip).limit(limit).all()

def create_cancha(db: Session, cancha: CanchaCreate):
    db_cancha = Cancha(**cancha.model_dump())
    db.add(db_cancha)
    db.commit()
    db.refresh(db_cancha)
    return db_cancha

def update_cancha(db: Session, cancha_id: int, cancha: CanchaUpdate):
    db_cancha = get_cancha(db, cancha_id)
    if not db_cancha:
        return None
    for key, value in cancha.model_dump(exclude_unset=True).items():
        setattr(db_cancha, key, value)
    db.commit()
    db.refresh(db_cancha)
    return db_cancha

def delete_cancha(db: Session, cancha_id: int):
    db_cancha = get_cancha(db, cancha_id)
    if db_cancha:
        db.delete(db_cancha)
        db.commit()
        return True
    return False
