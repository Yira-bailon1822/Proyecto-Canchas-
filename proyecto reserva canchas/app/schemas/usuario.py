from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str | None = None
    activo: bool = True

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    email: EmailStr | None = None
    telefono: str | None = None
    activo: bool | None = None

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
