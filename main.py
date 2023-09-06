from fastapi import FastAPI
from router.router import pais

app = FastAPI(
    title="CHALLENGE",
    description="API desarrollada con FastAPI para dar respuesta a ejercicio 'challenge' de Mercado Libre." ,
    version="FastAPi v0.1.0",
    )
app.include_router(pais)