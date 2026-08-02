from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.exceptions import EntityNotFoundException, BusinessRuleException
from app import crud

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if crud.usuario.get_usuario_by_email(db, usuario.email):
        raise BusinessRuleException("El correo electronico ya se encuentra registrado.")
    return crud.usuario.create_usuario(db=db, usuario=usuario)

@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.usuario.get_usuarios(db=db, skip=skip, limit=limit)

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.usuario.get_usuario(db=db, usuario_id=usuario_id)
    if not db_usuario:
        raise EntityNotFoundException("Usuario", usuario_id)
    return db_usuario

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = crud.usuario.update_usuario(db=db, usuario_id=usuario_id, usuario=usuario)
    if not db_usuario:
        raise EntityNotFoundException("Usuario", usuario_id)
    return db_usuario

@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    if not crud.usuario.delete_usuario(db=db, usuario_id=usuario_id):
        raise EntityNotFoundException("Usuario", usuario_id)
