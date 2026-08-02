from fastapi import FastAPI
from app.config import settings
from app.database import engine, Base
from app.routers import cancha, reserva, usuario

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API para la gestion de canchas deportivas y reservas.",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(cancha.router)
app.include_router(usuario.router)
app.include_router(reserva.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"mensaje": "API del Sistema de Reservas activa"}
