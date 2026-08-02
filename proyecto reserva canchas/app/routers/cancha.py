from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.cancha import CanchaCreate, CanchaUpdate, CanchaResponse
from app.exceptions import EntityNotFoundException
from app import crud

router = APIRouter(prefix="/canchas", tags=["Canchas"])

@router.post("/", response_model=CanchaResponse, status_code=status.HTTP_201_CREATED)
def crear_cancha(cancha: CanchaCreate, db: Session = Depends(get_db)):
    return crud.cancha.create_cancha(db=db, cancha=cancha)

@router.get("/", response_model=list[CanchaResponse])
def listar_canchas(
    tipo_deporte: str | None = Query(None),
    activa: bool | None = Query(None),
    precio_maximo: float | None = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.cancha.get_canchas(
        db=db,
        tipo_deporte=tipo_deporte,
        activa=activa,
        precio_maximo=precio_maximo,
        skip=skip,
        limit=limit
    )

@router.get("/{cancha_id}", response_model=CanchaResponse)
def obtener_cancha(cancha_id: int, db: Session = Depends(get_db)):
    db_cancha = crud.cancha.get_cancha(db=db, cancha_id=cancha_id)
    if not db_cancha:
        raise EntityNotFoundException("Cancha", cancha_id)
    return db_cancha

@router.put("/{cancha_id}", response_model=CanchaResponse)
def actualizar_cancha(cancha_id: int, cancha: CanchaUpdate, db: Session = Depends(get_db)):
    db_cancha = crud.cancha.update_cancha(db=db, cancha_id=cancha_id, cancha=cancha)
    if not db_cancha:
        raise EntityNotFoundException("Cancha", cancha_id)
    return db_cancha

@router.delete("/{cancha_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cancha(cancha_id: int, db: Session = Depends(get_db)):
    if not crud.cancha.delete_cancha(db=db, cancha_id=cancha_id):
        raise EntityNotFoundException("Cancha", cancha_id)
