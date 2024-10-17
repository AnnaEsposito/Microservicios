
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.models import pibData
from src.gdp_extractor.database import get_db

obtener_datos_pib_router = APIRouter()

@obtener_datos_pib_router.get("/gdp/")
async def obtener_datos_pib(pais: str, año: int, db: Session = Depends(get_db)):
    # Consultar la base de datos para el país y año dados
    datos_pib = db.query(pibData).filter(pibData.pais == pais, pibData.año == año).first()

    # Verificar si se encontraron datos
    if datos_pib is None:
        raise HTTPException(status_code=404, detail="Datos no encontrados, parametros requeridos [pais] y [año]")

    # Retornar los datos
    return {
        "pais": datos_pib.pais,
        "año": datos_pib.año,
        "pib_valor": datos_pib.pib_valor
    }
