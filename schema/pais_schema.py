from pydantic import BaseModel

class PaisSchema(BaseModel):
    nombre_pais: str
    capital: str
    poblacion: int