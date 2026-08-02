from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.cancha import CanchaCreate, CanchaResponse
from app.crud import cancha as crud_cancha

router = APIRouter(prefix="/canchas", tags=["Canchas"])

@router.post("/", response_model=CanchaResponse, status_code=status.HTTP_201_CREATED)
def create_cancha(cancha: CanchaCreate, db: Session = Depends(get_db)):
    return crud_cancha.create_cancha(db=db, cancha=cancha)

@router.get("/", response_model=List[CanchaResponse])
def read_canchas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_cancha.get_canchas(db, skip=skip, limit=limit)