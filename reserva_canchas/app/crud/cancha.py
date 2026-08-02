from sqlalchemy.orm import Session
from app.models.cancha import CanchaModel
from app.schemas.cancha import CanchaCreate

def get_canchas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CanchaModel).offset(skip).limit(limit).all()

def create_cancha(db: Session, cancha: CanchaCreate):
    db_cancha = CanchaModel(**cancha.model_dump())
    db.add(db_cancha)
    db.commit()
    db.refresh(db_cancha)
    return db_cancha