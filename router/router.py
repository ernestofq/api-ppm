from fastapi import APIRouter
from schema.pais_schema import PaisSchema
from config.db import conn
from model.paises import paises
from fastapi import HTTPException
import httpx


pais = APIRouter()


@pais.get("/", summary="Obtener datos solicitados según requerimiento.")
def obtener_datos_exigidos_en_el_challenge(nombre_pais: str):
    pais = conn.execute(paises.select().where(paises.c.nombre_pais == nombre_pais)).first()
    if pais != None:
        poblacionMundial = 8000000000    #Asumiendo este valor como total de poblacion mundial, se podria calcular sumando la poblacion de todos los paises en la BD, pero si la BD estubiera incompleta el resultado del porcentaje que corresponde a un pais podria alejarse demasiado de la realidad ya que se calcula en base al total de poblacion
        porcentaje = (pais[2]*100)/poblacionMundial
        porcentaje = str(porcentaje)
        porcentaje = porcentaje+"%"
        siguentePaisMasPoblado = conn.execute(paises.select().where(paises.c.poblacion > pais[2]).order_by(paises.c.poblacion)).first()
        conn.commit()
        if siguentePaisMasPoblado == None:
            resultado = {"capital": pais[1],"porcentaje_mundial": porcentaje, "siguiente_pais_mas_poblado": "No existe un pais mas poblado que "+pais[0]}
        else:
            resultado = {"capital": pais[1],"porcentaje_mundial": porcentaje, "siguiente_pais_más_poblado": siguentePaisMasPoblado[0]}
        return resultado
    else:
        return HTTPException(status_code=404, detail="Compruebe que haya escrito correctamente el nombre del país. Este nombre de país no se encuentra en nuestra base.")

"""
@pais.post("/agregado/manual")
def agregar_pais_manualmente(datosPais: PaisSchema):
    nuevoPais = datosPais.dict()
    #me falta validar que el dato que voy a insertar no exista
    result = conn.execute(paises.insert().values((datosPais.nombre_pais, datosPais.capital, datosPais.poblacion)))
    conn.commit()
    return nuevoPais
"""

@pais.get("/agregado/automatico", summary="LLenar la BD con los datos de los paises.")
def llenar_bd():
    url = f"https://restcountries.com/v3.1/all"
    with httpx.Client() as cliente:
        respuesta = cliente.get(url)
        if respuesta.status_code == 200:
            respuesta_json = respuesta.json()
            temp = 1
            for elemento in respuesta_json:
                if "name" in elemento and "common" in elemento["name"]:
                    nombrePais = elemento["name"]["common"]
                else:
                    nombrePais = "Nombre de país desconocido"
                if "capital" in elemento:
                    capitalPais = elemento["capital"][0]
                else:
                    capitalPais = "Capital desconocida"
                if "population" in elemento:
                    poblacionPais = elemento["population"]
                else:
                    poblacionPais = "Población desconocida"
                if conn.execute(paises.select().where(paises.c.nombre_pais == nombrePais)).first() == None:
                    conn.execute(paises.insert().values((nombrePais, capitalPais, poblacionPais)))
                    temp = 2
                conn.commit()
            if temp == 1:
                return HTTPException(status_code=respuesta.status_code, detail="La Base de Datos no necesitaba actualización")
            else:
                return HTTPException(status_code=respuesta.status_code, detail="Datos recopilados y salvados en Base de Datos.")
        else:
            return HTTPException(status_code=respuesta.status_code, detail="Error al intentar consultar el sitio restcountries.com.")
