from fastapi import FastAPI
from app.routers import cancha
from app.database import Base, engine

# Crea las tablas en la BD al arrancar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Sistema de Reservas de Canchas",
    version="1.0.0"
)

app.include_router(cancha.router)

@app.get("/")
def home():
    return {"mensaje": "API lista para usar"}