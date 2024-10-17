from fastapi import FastAPI
from src.gdp_extractor.router.router import router as obtener_datos_pib_router

app = FastAPI()

# Registrar los microservicios
app.include_router(obtener_datos_pib_router, prefix="/extractor")
#app.include_router(gdp_comparator_router, prefix="/comparator")

@app.get("/")
async def root():
    return {"message": "Microservicios de PIB en funcionamiento"}

