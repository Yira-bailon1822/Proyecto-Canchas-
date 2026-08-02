from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.reserva import ReservaCreate, ReservaUpdate, ReservaResponse
from app import crud

router = APIRouter(prefix="/reservas", tags=["Reservas"])

@router.post("/", response_model=ReservaResponse, status_code=status.HTTP_201_CREATED)
def crear_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    return crud.reserva.create_reserva(db=db, reserva=reserva)

@router.get("/", response_model=list[ReservaResponse])
def listar_reservas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.reserva.get_reservas(db=db, skip=skip, limit=limit)

@router.get("/{reserva_id}", response_model=ReservaResponse)
def obtener_reserva(reserva_id: int, db: Session = Depends(get_db)):
    return crud.reserva.get_reserva(db=db, reserva_id=reserva_id)

@router.put("/{reserva_id}", response_model=ReservaResponse)
def actualizar_reserva(reserva_id: int, reserva: ReservaUpdate, db: Session = Depends(get_db)):
    return crud.reserva.update_reserva(db=db, reserva_id=reserva_id, reserva=reserva)

@router.delete("/{reserva_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    crud.reserva.delete_reserva(db=db, reserva_id=reserva_id)
